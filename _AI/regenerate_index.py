#!/usr/bin/env python3
"""
Regenerate the Library indexes from frontmatter.

Run after any import:  python3 _AI/regenerate_index.py

Writes two files:
  Library/Conversation Index.md        non-sensitive only — committed to git
  Library/Private Index.private.md     sensitive only — gitignored

The split matters. Both indexes list filenames and titles, and the slugs describe
their contents. Putting sensitive notes in the committed index would republish the
exact filenames .gitignore exists to keep out of the repo. The private index carries
the .private.md suffix so the same wildcard rule covers it.

Also reports integrity problems rather than silently fixing them:
  - sensitive: true without the .private.md suffix  (WOULD BE COMMITTED)
  - .private.md suffix without sensitive: true      (inconsistent metadata)
  - missing or unknown category
"""
import re, glob, os, sys, collections, datetime, subprocess

LIB = 'Library'
META = {'Import Schema', 'About the Library', 'Conversation Index', 'Private Index.private'}

CATEGORIES = {
    "Coding & Dev Projects", "Home Lab, Networking & Smart Home", "Finance & Investing",
    "Health & Fitness", "Style & Grooming", "Career & Work", "Relationships & Social",
    "Design & Creative", "Home, Apartment & Shopping", "Tech Support (General)",
    "Cars & Vehicles", "Sports & Entertainment", "Food & Recipes",
    "Learning & Reference", "General & Life Admin",
}


def field(fm, key):
    m = re.search(rf'^{key}:\s*(.+)$', fm, re.M)
    return m.group(1).strip().strip('"') if m else ''


def main():
    pub, priv, unfiled, problems = (collections.defaultdict(list),
                                    collections.defaultdict(list), [], [])
    sources = set()

    for p in sorted(glob.glob(f'{LIB}/*.md')):
        stem = os.path.splitext(os.path.basename(p))[0]
        if stem in META:
            continue
        t = open(p, encoding='utf-8').read()
        m = re.match(r'^---\n(.*?)\n---', t, re.S)
        if not m:
            problems.append(f'NO FRONTMATTER      {p}')
            continue
        fm = m.group(1)
        sensitive = field(fm, 'sensitive').lower() == 'true'
        suffixed = stem.endswith('.private')
        cat, title, date = field(fm, 'category'), field(fm, 'title') or stem, field(fm, 'date')
        if field(fm, 'source'):
            sources.add(field(fm, 'source'))

        if sensitive and not suffixed:
            problems.append(f'!! WOULD BE COMMITTED  {p}  (sensitive: true, needs .private.md suffix)')
        if suffixed and not sensitive:
            problems.append(f'INCONSISTENT        {p}  (.private.md suffix but sensitive is not true)')
        if not cat:
            unfiled.append((date, stem, title))
        elif cat not in CATEGORIES:
            problems.append(f'UNKNOWN CATEGORY    {p}  ({cat!r})')
        else:
            (priv if sensitive else pub)[cat].append((date, stem, title))

    today = datetime.date.today().isoformat()
    src = ', '.join(sorted(sources)) or '—'

    def render(groups, title_, blurb, extra=()):
        total = sum(len(v) for v in groups.values())
        out = ['---', f'title: {title_}', 'type: meta', '---', '', f'# {title_}', '', blurb, '',
               f'**Conversations:** {total} &nbsp;|&nbsp; **Categories:** {len(groups)}'
               f' &nbsp;|&nbsp; **Sources:** {src}', '', f'*Generated {today} '
               'by `_AI/regenerate_index.py` — regenerate, do not hand-edit.*', '']
        out += list(extra)
        for cat in sorted(groups):
            rows = sorted(groups[cat])
            out += [f'## {cat} ({len(rows)})', '']
            out += [f'- `{d}` [[{s}]] — {ti}' for d, s, ti in rows]
            out.append('')
        return '\n'.join(out), total

    unfiled_block = []
    if unfiled:
        unfiled_block = [f'## ⚠️ Unfiled ({len(unfiled)})', '', 'No `category` set.', '']
        unfiled_block += [f'- [[{s}]] — {ti}' for _, s, ti in sorted(unfiled)] + ['']

    body, n_pub = render(pub, 'Conversation Index',
                         'Browsable listing of the non-sensitive conversation corpus, grouped by category.\n'
                         'Sensitive conversations are indexed separately in `Private Index.private.md`,\n'
                         'which is gitignored — listing them here would republish the filenames that\n'
                         '`.gitignore` exists to keep out of the repo.', unfiled_block)
    open(f'{LIB}/Conversation Index.md', 'w', encoding='utf-8').write(body)

    n_priv = 0
    if priv:
        body, n_priv = render(priv, 'Private Index',
                              'Sensitive conversations (health, financial, family, legal/work).\n'
                              'This file is gitignored via the `.private.md` suffix. Do not rename it.')
        open(f'{LIB}/Private Index.private.md', 'w', encoding='utf-8').write(body)

    print(f'  public index : {n_pub} conversations')
    print(f'  private index: {n_priv} conversations' + ('' if priv else '  (not written — none present)'))
    print(f'  unfiled      : {len(unfiled)}')

    # Verify git actually ignores every sensitive file — belt and braces.
    sens = [p for p in glob.glob(f'{LIB}/*.private.md')]
    if sens:
        r = subprocess.run(['git', 'check-ignore'] + sens, capture_output=True, text=True)
        ignored = set(r.stdout.split('\n'))
        leaks = [p for p in sens if p not in ignored]
        print(f'  git-ignored  : {len(sens) - len(leaks)}/{len(sens)} sensitive files')
        for p in leaks:
            problems.append(f'!! NOT GITIGNORED      {p}')

    if problems:
        print('\n  PROBLEMS:')
        for p in problems:
            print('   ', p)
        return 1
    print('\n  no problems found')
    return 0


if __name__ == '__main__':
    sys.exit(main())
