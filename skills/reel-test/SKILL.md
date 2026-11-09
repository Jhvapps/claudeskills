---
name: reel-test
description: >
  Mandatory test-and-deliver step for EVERY reel or short video made in Jack's stack (Remotion renders,
  Higgsfield video, edited clips). Scores it on Higgsfield's Virality Predictor, applies the pass mark
  (60 overall, 50 hook), does one rework round if below, then uploads the reel to the shared Reels Drive
  folder and adds its caption + hashtags row to the "Reel captions" Google Sheet. Use whenever a reel is
  rendered, before sending any video to Jack, or when he says "test this reel", "will this get followers",
  "score this", "virality", "put it in the Drive".
---

# Reel test (approved by Jack 2026-11-09)

Soft gate. Every reel is tested before delivery. A hook blocks SendUserFile for any .mp4/.mov without a
`<file>.score.json` next to it, and reminds you after every `remotion render`.

## Rules
- Pass mark: **overall >= 60 AND hook >= 50**. Set in `score.py` (PASS_OVERALL, PASS_HOOK).
- Below the pass mark: do **one** rework round aimed at what the report shows (weak hook = first 3s;
  drop-off second = cut or speed up that scene), re-render, re-test, then deliver with the score and a flag.
  Never loop more than once without Jack.
- The test scores the video as uploaded. If the reel will get audio in Instagram, say the score is silent.
- Scores are a proxy. Never tell Jack a reel "will get followers"; give the score and the weak seconds.
- If Higgsfield is down, `score.py --skip "reason"` writes the sidecar so delivery can go ahead, and tell Jack.

## Steps
1. **Upload** (Higgsfield MCP): `media_upload` (type video) returns a presigned URL. Then
   `curl -X PUT -H "Content-Type: video/mp4" -H "If-None-Match: *" --data-binary @FILE "URL"`
   (`If-None-Match` is a signed header, it must be sent), then `media_confirm`.
   The `higgsfield` CLI cannot run this model (text models unsupported as of CLI 1.2.2), so use the MCP.
2. **Test**: `virality_predictor` with the media id. Max 2 jobs at once. `jobs_wait` until done.
3. **Save the report** HTML from the result URL with curl into the scratchpad.
4. **Score**:
   `python3 -I ~/.claude/skills/reel-test/score.py REPORT.html VIDEO.mp4 --brand "<Brand>" --name "<Reel>" --version v1`
   Exit 0 = PASS, 2 = BELOW. It writes `VIDEO.mp4.score.json`, appends a row to the vault log
   (`50 Stack/Reel scores.md`; Coal & Co brands go to `~/repos/coalandco-vault/Reel scores.md`), and prints
   the weakest seconds and drop-off second.
5. **Rework once if BELOW**, then repeat 1-4 with `--version v2`.
6. **Drive**: upload the final reel to the Reels folder, name `<brand-slug>_<YYYY-MM>_<n>-<reel-slug>.mp4`:
   `rclone copy FILE "jackdrive,root_folder_id=1IkxfxLUfRM_hXQkFR5yCgfCXL6uHz_hs:"`
   (inline remote syntax; zsh will not split a `--drive-root-folder-id` variable).
   Folder: https://drive.google.com/drive/folders/1IkxfxLUfRM_hXQkFR5yCgfCXL6uHz_hs
7. **Captions sheet**: append one row with the Google Sheets MCP `append_values` to spreadsheet
   `1hTxVMwYE6AcmjJkbeEVPMMWqCHGysgepAWvsgudmGPc`, range `A1`. Columns:
   Date made | Brand | Reel | File (this folder) | Post as | Caption | Hashtags | Virality overall |
   Virality hook | Verdict | Posted on | IG views 48h | IG follows 48h (leave the last three blank).
   Caption: hook line first, short lines, one CTA, brand voice, **no em-dashes**. 8-10 hashtags, local first.
8. **Deliver**: SendUserFile the reel with the score in the caption, and give Jack the Drive folder link.

## Brand facts
- Chef Burger: @chefburgeruk, Eastbourne/Sussex, tagline "Grill. Graft. Glory."
