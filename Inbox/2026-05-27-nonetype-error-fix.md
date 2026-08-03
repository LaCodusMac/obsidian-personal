---
date: 2026-05-27
source: chatgpt
title: "NoneType Error Fix"
category: "Coding & Dev Projects"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** ⚠️ 'NoneType' object is not iterable

**ChatGPT:** That error means your code is trying to loop over (`for ... in ...`) something that is actually `None`.

A common example:

```python
items = None

for item in items:
    print(item)
```

This raises:

```python
TypeError: 'NoneType' object is not iterable
```

### How to fix it

Check why the variable is `None` before iterating.

#### Option 1: Provide a default empty list

```python
for item in items or []:
    print(item)
```

#### Option 2: Check explicitly

```python
if items is not None:
    for item in items:
        print(item)
```

#### Option 3: Trace where `None` comes from

Often this happens because:

- a function forgot to `return`
- an API/database call failed
- `.get()` returned `None`
- a variable was overwritten

Example:

```python
def get_data():
    pass

data = get_data()

for x in data:   # error
    print(x)
```

Fix:

```python
def get_data():
    return []
```

If you paste the code causing the error, I can point to the exact line and fix it.
