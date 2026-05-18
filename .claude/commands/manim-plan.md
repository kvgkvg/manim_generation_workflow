# Command: /manim-plan
# Usage: /manim-plan <section_name>
# Example: /manim-plan 01_diffusion_basics
#
# What it does:
#   1. Validates content/<section>/ has PDF + transcript
#   2. Reads and analyzes both files
#   3. Generates sections/<section>/SCRIPT.md
#   4. Generates sections/<section>/VOICEOVER.md
#   5. Presents scene table for user review
#   6. Waits for confirmation before any rendering

---

## STEP 0 — Parse section name

```bash
SECTION="$1"   # e.g. "01_diffusion_basics"

if [ -z "$SECTION" ]; then
    echo "Usage: /manim-plan <section_name>"
    echo ""
    echo "Available sections in content/:"
    ls content/ 2>/dev/null || echo "  (content/ folder not found)"
    exit 1
fi

echo "Planning section: $SECTION"
```

---

## STEP 0.5 — Ask user for duration target

Before reading any files, ask:

```
Before I analyze the content, I need one input from you:

  How long should this section be?

  Common choices:
    [1]  ~5 min   — intro / overview / short concept
    [2]  ~8 min   — standard section
    [3]  ~12 min  — detailed / equation-heavy section
    [4]  ~15 min  — full deep-dive
    [5]  Custom   — tell me a number in minutes

  (This determines how many scenes I create and how much
  detail goes into each one.)
```

Wait for user response. Parse into `TARGET_MINUTES`:
- "5" / "5 min" / "[1]" → `TARGET_MINUTES=5`
- "8" / "[2]" → `TARGET_MINUTES=8`
- "12" / "[3]" → `TARGET_MINUTES=12`
- "15" / "[4]" → `TARGET_MINUTES=15`
- Any other number → use that value

Then confirm back:
```
Got it — targeting ~{TARGET_MINUTES} minutes for this section.
That's roughly {TARGET_MINUTES * 60} seconds total,
which I'll split into approximately {estimate_scenes(TARGET_MINUTES)} scenes.

Proceeding to analyze content/...
```

Scene count estimation:
```python
def estimate_scenes(minutes):
    seconds = minutes * 60
    # Title ~8s, outro ~20s, average body scene ~45s
    body_seconds = seconds - 8 - 20
    return 2 + max(1, round(body_seconds / 45))
# 5 min  → ~8 scenes
# 8 min  → ~12 scenes
# 12 min → ~17 scenes
# 15 min → ~21 scenes
```

Store `TARGET_MINUTES` — it will be used in STEP 4 and STEP 6.

---

## STEP 1 — Validate input files

```bash
python3 - << EOF
import os, glob, sys

section = "$SECTION"
content_dir = f"content/{section}"

if not os.path.isdir(content_dir):
    print(f"ERROR: content/{section}/ not found")
    print(f"Available sections: {os.listdir('content') if os.path.exists('content') else 'content/ missing'}")
    sys.exit(1)

# Find PDF
pdfs = glob.glob(f"{content_dir}/*.pdf")
txts = glob.glob(f"{content_dir}/*.txt")

if not pdfs:
    print(f"ERROR: No .pdf found in {content_dir}/")
    sys.exit(1)
if not txts:
    print(f"ERROR: No .txt found in {content_dir}/")
    sys.exit(1)

print(f"PDF      : {pdfs[0]}")
print(f"Transcript: {txts[0]}")
print("Input files OK.")
EOF
```

---

## STEP 2 — Read PDF slides

```bash
pip install pdfplumber --break-system-packages -q 2>/dev/null

python3 - << EOF
import pdfplumber, glob

section = "$SECTION"
pdf_file = glob.glob(f"content/{section}/*.pdf")[0]

print(f"=== PDF: {pdf_file} ===\n")
with pdfplumber.open(pdf_file) as pdf:
    for i, page in enumerate(pdf.pages):
        text = (page.extract_text() or "").strip()
        if text:
            print(f"--- Slide {i+1} ---")
            print(text[:600])
            print()
EOF
```

---

## STEP 3 — Read transcript

```bash
python3 - << EOF
import glob

section = "$SECTION"
txt = glob.glob(f"content/{section}/*.txt")[0]
content = open(txt, encoding='utf-8', errors='replace').read()
print(f"=== Transcript: {txt} ({len(content)} chars) ===\n")
print(content[:4000])
if len(content) > 4000:
    print(f"\n... [{len(content)-4000} more chars] ...")
EOF
```

---

## STEP 4 — Analysis pass (think before writing)

Before generating any scene, identify:

```
CONCEPTS  : every distinct concept explained (list them)
EQUATIONS : every equation shown, with exact LaTeX from slides
VISUALS   : every diagram/figure and what it shows
FLOW      : transcript section → slide → concept order
```

Then plan scenes using `TARGET_MINUTES` as hard constraint:

```
Total budget  : TARGET_MINUTES × 60 seconds
Title card    : 8s   (fixed)
Outro         : 20s  (fixed)
Body budget   : remaining seconds

Scene count   : estimate_scenes(TARGET_MINUTES)
Avg body scene: body_budget / (scene_count - 2) seconds

Packing rule:
- If content is dense (many equations): fewer scenes, more depth each
- If content is visual (many diagrams):  more scenes, lighter each
- Never exceed 60s per scene — split if needed
- Never go below 20s per scene — merge if too thin
```

Write out the planned scene list before generating SCRIPT.md:
```
Scene 1  — Title Card         8s
Scene 2  — [concept]         Xs   ← derived from budget
Scene 3  — [concept]         Xs
...
Scene N  — Summary           20s
─────────────────────────────────
Total                        ~TARGET_MINUTES min
```

If the content doesn't fill the target duration naturally,
**do not pad with filler** — instead tell the user:
```
Note: the content covers about X minutes of material.
I'll generate a tight X-minute script rather than padding to {TARGET_MINUTES} min.
```

---

## STEP 5 — Create output directory

```bash
mkdir -p sections/$SECTION
echo "Created sections/$SECTION/"
```

---

## STEP 6 — Generate SCRIPT.md

Write to `sections/$SECTION/SCRIPT.md` following this format exactly:

```markdown
# SCRIPT.md — [Human-readable section title] Manim Video
**Section:** `[section_folder_name]`
**Target duration:** ~[TARGET_MINUTES] minutes ([TARGET_MINUTES×60]s)
**Scene count:** [N] scenes
**Style:** 3Blue1Brown · dark bg · no voiceover
**Manim version:** Community Edition v0.19
**Color palette:** WHITE, BLUE, GREEN, RED, YELLOW, ORANGE (built-ins only)

<!-- Duration budget:
     Title  :   8s  (Scene 1, fixed)
     Body   :  [X]s ([N-2] scenes × ~[avg]s each)
     Outro  :  20s  (Scene N, fixed)
     Total  : ~[TARGET_MINUTES×60]s
-->

---

## NOISE IMPLEMENTATION
[Always include — NoisySquare uses PIL ImageMobject, NOT fill_color=WHITE]

Key rule: t_ratio=0.0 → clean GREEN, t_ratio=1.0 → pure TV static noise.
Green channel must reach 0 at t_ratio=1.0 — no color tint on pure noise.
Full implementation is in shared/utils.py.

---

## LAYOUT SAFETY RULES
- All objects: x in [-6.5, 6.5], y in [-3.5, 3.5]
- Labels: always .next_to(ref, DIR, buff=0.3) — no hardcoded y near other elements
- Two text objects at same y: must have horizontal separation ≥ 2.0
- Font sizes: title=44, body=30–34, label=22–26, tiny=18–20
- VGroup too wide: .scale_to_fit_width(11.5)
- Verify layout sketch before writing each scene:
    y= 3.0  top limit
    y= 2.x  labels/titles
    y= 1.x  equations
    y= 0.x  main visuals
    y=-1.x  secondary
    y=-2.x  captions
    y=-3.0  bottom limit

---

## SCENE 1 — [Title]
**Class:** `Scene1` · **Target:** Xs

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `obj_name` | 1.0 | `ExactManimCode(...)`, position |
...

**Layout:**
[sketch y-positions of all elements, confirm no overlap]

---
[repeat for each scene]
```

Action types allowed: `fade_in` `fade_out` `write` `create` `move` `highlight` `wait` `transform`

Action → Manim:
- `write` → `self.play(Write(obj))`
- `create` → `self.play(Create(obj))`
- `fade_in` → `self.play(FadeIn(obj))`
- `fade_out` → `self.play(FadeOut(obj))`
- `move` → `self.play(obj.animate.shift(DIR*n))`
- `highlight` → `self.play(Indicate(obj, color=C, scale_factor=1.2))`
- `wait` → `self.wait(n)`

---

## STEP 7 — Generate VOICEOVER.md

Write to `sections/$SECTION/VOICEOVER.md`:

```markdown
# VOICEOVER.md — [Section title]
What to say when recording. Use as guide, not script to read verbatim.

## SCENE 1 — [Title] (~Xs)
[When animation appears]: what to say

## SCENE 2 — [Title] (~Xs)
[Cue]: content
...

## Recording tips
- Watch video once before recording
- Pause after each animation step — don't rush
- Equation-heavy scenes: pause after each term
```

---

## STEP 8 — Present scene table to user

```
✓ Generated: sections/{SECTION}/SCRIPT.md
✓ Generated: sections/{SECTION}/VOICEOVER.md

Scene plan for "{SECTION}"  [target: ~{TARGET_MINUTES} min]

┌──────────────────────────────────────────────────────────────────┐
│  #  │ Scene Title                    │ Duration │ Key Visual     │
├──────────────────────────────────────────────────────────────────┤
│  1  │ Title Card                     │   8s     │ Text           │
│  2  │ [concept from transcript]      │  Xs ←┐  │ [visual type]  │
│  3  │ [concept]                      │  Xs  │  │ [equation]     │
│ ... │ ...                            │  ... │  │ ...            │
│  N  │ Summary & Outro                │  20s │  │ Summary boxes  │
├───────────────────────────────────── │ ─────┘  ├────────────────┤
│     │ TOTAL                          │ ~{TARGET_MINUTES} min    │
│     │ Budget remaining               │ {slack}s slack           │
└──────────────────────────────────────────────────────────────────┘

Equations found : [list from slides]
Key visuals     : [list from slides]
Content density : [light / medium / heavy — affects avg scene length]

Ready to render?
  /manim-render {SECTION} all          → render all scenes
  /manim-render {SECTION} scene 2      → render one scene
  /manim-render {SECTION} scene 2 3 5  → render specific scenes

Or tell me which scenes to adjust, or change the target duration.
```

**Stop here. Wait for user response.**
