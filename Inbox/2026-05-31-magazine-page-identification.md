---
date: 2026-05-31
source: chatgpt
title: "Magazine Page Identification"
category: "Design & Creative"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** {"asset_pointer": "sediment://file_00000000437871f5919a0b0207f6c953", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 504946, "width": 1152}
Help me identify where this is from

**ChatGPT:** This looks like a page from a magazine, and there are some useful clues visible in the image:

- Bottom right: **"PICTORIAL LIVING COLOROTO MAGAZINE, Nov. 10, 1974 — 33"**
- Photo credit: **"Photo by Bob Howard"**
- Caption:
  > "Lowell Tech's offensive halfback Brian Connolly breaks through the line of Bentley College as he racks up some yardage for a 1st down."

From that, we can identify it pretty confidently as:

- **Pictorial Living Coloroto Magazine**
- **November 10, 1974 issue**
- **Page 33**
- Covering a football game between **Lowell Technological Institute** (now part of entity["organization","University of Massachusetts Lowell","formerly Lowell Technological Institute"]) and entity["organization","Bentley University","formerly Bentley College"].
- The player shown is identified as **Brian Connolly**, a Lowell Tech halfback.

### What is "Coloroto"?
The word appears to be a printing style or regional publication title. Given the age and typography, it may actually be "Colorado" or another title obscured by the photo quality. The page itself looks like a New England college sports feature because Lowell Tech and Bentley are both Massachusetts schools.

### If you're trying to determine why you have it
This would most likely have come from:
- A former Lowell Tech athlete or alumnus
- A Bentley alumnus
- A scrapbook or keepsake from the 1974 football season
- A local Massachusetts sports or alumni publication

If you'd like, I can also help:
1. Track down the full November 10, 1974 issue.
2. Find records of the Lowell Tech vs. Bentley game.
3. Research Brian Connolly and see whether he was a notable player at Lowell Tech.

**You:** Help me track down that issue

**ChatGPT:** I dug into it, and I think the key clue is actually the publication title.

The page clearly shows:

> **"PICTORIAL LIVING COLOROTO MAGAZINE"**  
> Nov. 10, 1974 — Page 33

The problem is that "Coloroto" doesn't appear to be a well-known magazine title, which makes me suspect one of three things:

1. The title is partially obscured or distorted by the age of the paper and photo.
2. It was a regional Sunday magazine insert distributed with a local newspaper.
3. It was a short-lived New England publication that isn't well digitized.

What we do know for certain from the page itself:

- Date: **November 10, 1974**
- Page: **33**
- Photographer: **Bob Howard**
- Subject: **Lowell Tech vs. Bentley College football**
- Player identified: **Brian Connolly, Lowell Tech halfback**

That points strongly toward a Massachusetts regional publication rather than a national magazine. citeturn0search18

### Places I'd check next

#### UMass Lowell Archives
Since the article features Lowell Tech athletics, the university archives are probably the best lead.

urlUMass Lowell Archives & Special Collectionshttps://www.uml.edu/library/archives/

Ask:

> "Do you have a copy of Pictorial Living Coloroto Magazine, Nov. 10, 1974, page 33, featuring Brian Connolly and the Lowell Tech vs Bentley football game?"

#### Bentley Archives
Bentley maintains historical collections and yearbooks.

urlBentley University Archiveshttps://www.bentley.edu/library/archives-special-collections

#### Lowell Sun Archives
A lot of regional sports photography ended up in Sunday magazine supplements associated with local newspapers.

urlThe Lowell Sunhttps://www.lowellsun.com

### One thing I'd like to verify

Can you take a close-up photo of:
- the **bottom-right corner** where the magazine title appears, and
- the **entire back side** of the page?

A sharper image of the masthead will probably let me identify the exact publication and potentially locate a digitized copy of the whole issue. Right now, the publication title is the only piece that's still uncertain.

**You:** {"asset_pointer": "sediment://file_0000000039fc722f8b3d0af385859327", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 498154, "width": 1152}
{"asset_pointer": "sediment://file_000000004428722fb804a8ba48b4d5d0", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 654189, "width": 1152}

**ChatGPT:** That second photo solves the mystery.

The publication is **Pictorial Living Coloroto Magazine**, and based on the layout, ads, and mailing label section ("Berenson's"), this appears to have been a **Sunday newspaper magazine insert distributed in the Lowell, Massachusetts area** in the 1970s rather than a standalone national magazine.

The strongest clues:

- Date: **November 10, 1974**
- Page numbers visible: **33–34**
- Local advertisers:
  - Berenson's
  - Nashua Pie Company
  - References to Boston and Lowell-area businesses
- Sports content featuring **Lowell Tech vs. Bentley**
- Local photographer credit (**Bob Howard**)

My best guess is that this was inserted into either:
- The **Lowell Sun**
- The **Nashua Telegraph**
- Another Merrimack Valley Sunday paper

The fact that page 34 is a recipe page with local ads is exactly the kind of content Sunday newspaper magazines carried.

### What I'd do next

1. Contact the Lowell Sun archives:
   - Ask whether they carried **Pictorial Living Coloroto Magazine** on Nov. 10, 1974.

2. Contact UMass Lowell archives:
   - Ask if they have the Nov. 10, 1974 issue containing coverage of the Bentley game.

3. Search newspaper microfilm for Nov. 10, 1974:
   - entity["organization","Lowell Public Library","Lowell, MA, USA"]
   - entity["organization","UMass Lowell Archives and Special Collections","Lowell, MA, USA"]

### Interesting historical detail

The caption identifies:

> "Brian Connolly"

running for **Lowell Tech**.

Since Lowell Tech merged with Lowell State in 1975 to become what is now entity["organization","University of Massachusetts Lowell","public university"], this page was printed during the final year before the merger. That makes it a neat piece of pre-UMass Lowell athletic history.

One thing I can do next is try to determine:
- the final score of the Lowell Tech vs. Bentley game,
- whether Brian Connolly appears in Lowell Tech football rosters from 1974,
- and whether a complete scan of this Nov. 10, 1974 issue exists in any archive.
