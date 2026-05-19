# CLAUDE.md — Manim Multi-Section Video Workflow

## Project structure

```
project/
├── CLAUDE.md
├── content/                        ← user provides, never modify
│   ├── 01_diffusion_basics/
│   │   ├── slides.pdf
│   │   └── transcript.txt
│   ├── 02_ddim/
│   │   ├── slides.pdf
│   │   └── transcript.txt
│   └── 03_latent_diffusion/
│       ├── slides.pdf
│       └── transcript.txt
│
├── sections/                       ← generated, one folder per section
│   ├── 01_diffusion_basics/
│   │   ├── SCRIPT.md
│   │   ├── VOICEOVER.md
│   │   ├── scene_1.py … scene_N.py
│   │   └── render_registry.txt
│   ├── 02_ddim/
│   │   └── ...
│   └── 03_latent_diffusion/
│       └── ...
│
├── shared/
│   ├── config.py                   ← shared constants
│   └── utils.py                    ← NoisySquare, NoiseTimeline, etc.
│
├── media/                          ← manim output (auto-generated)
└── output/
    ├── 01_diffusion_basics.mp4
    ├── 02_ddim.mp4
    └── final_output.mp4            ← full video all sections
```

---

## Commands

| Command | What it does |
|---|---|
| `/manim-plan <section>` | Analyze content/<section>/ → generate sections/<section>/SCRIPT.md → present to user |
| `/manim-render <section> all` | Render all scenes for a section |
| `/manim-render <section> scene 3` | Render one scene |
| `/manim-render <section> scene 2 4 7` | Render specific scenes |
| `/manim-render <section> resume` | Render only unfinished scenes |
| `/manim-compose <section>` | Assemble one section → output/<section>.mp4 |
| `/manim-compose all` | Assemble all sections → output/final_output.mp4 |
| `/manim-compose all hq` | Re-render everything at 1080p then assemble |

---

## shared/config.py

```python
BG_COLOR     = "#1C1C2E"
SQUARE_SIZE  = 1.0;   SQUARE_GAP  = 0.15
FONT_TITLE   = 48;    FONT_BODY   = 34
FONT_SMALL   = 24;    FONT_TINY   = 20
DEFAULT_FONT = "DejaVu Sans"   # always pass font=DEFAULT_FONT to every Text() call
```

---

## Hard rules for every scene file

| Rule | Requirement |
|---|---|
| Imports | `from manim import *` then `import sys, os; sys.path.insert(0, "../../shared"); from config import *; from utils import *` |
| Colors | Built-in names only · no hex · no CYAN |
| MathTex | Always `r"..."` raw strings |
| Text font | Always `Text("...", font=DEFAULT_FONT)` — never bare `Text("...")` |
| self.add() | FORBIDDEN — every object must enter via `self.play(FadeIn/Write/Create)` |
| Pacing | Every `self.play()` → `self.wait()` min 0.5s |
| Lifecycle | Never reference object after `FadeOut` |
| Layout | x:[-6.5,6.5] y:[-3.5,3.5] · prefer `.next_to()` over hardcoded coords |
| Noise | Always `NoisySquare(t_ratio)` — never `fill_color=WHITE` |
| End | Every `construct()` ends with `self.wait(2)` |
| Forbidden | `ThreeDScene` `add_updater` `always_redraw` `ValueTracker` `camera.frame.animate` |
| Output tag | Wrap in `<manim>...</manim>` |

---

## Quality flags

| Flag | Resolution | Use when |
|---|---|---|
| `-pql` | 480p 15fps | Dev / quick test |
| `-qh` | 1080p 60fps | Final output |

---

## Common errors

| Symptom | Fix |
|---|---|
| `LaTeX Error` | Add `r""` to MathTex |
| `NameError: CYAN` | Use `BLUE` or `WHITE` |
| Blank frame | Add `self.wait(2)` at end |
| Off-screen | `.scale_to_fit_width(12)` |
| Greenish noise | NoisySquare green channel must = 0 at t_ratio=1.0 |
| Text overlap | Use `.next_to(ref, DIR, buff=0.3)` |
| Import error | Check sys.path points to shared/ |
| Font spacing too wide | See TEXT RENDERING rules below |
| Objects appear too early | See OBJECT LIFECYCLE rules below |

---

## TEXT RENDERING (fix for wide character spacing)

Manim's default `Text()` uses Pango/Cairo which can produce wide letter-spacing
on some systems. Always use these rules:

```python
# ALWAYS specify font explicitly — never rely on system default
Text("Hello", font="Sans", font_size=34)

# For titles and body text — use these fonts in order of preference:
# 1. "Sans"          → clean, reliable cross-platform
# 2. "DejaVu Sans"   → good fallback on Linux
# 3. "Noto Sans"     → best Unicode coverage

# NEVER use:
Text("Hello")                    # no font specified → system default → wide spacing
Text("Hello", font="Arial")      # may not exist on Linux → fallback is unpredictable

# For multi-word labels that look too spread out:
# Add disable_ligatures=False and check font is installed:
import subprocess
subprocess.run(["fc-list"], capture_output=True)  # check available fonts

# To globally fix spacing — add to config.py:
DEFAULT_FONT = "Sans"

# Then in every scene:
Text("Hello", font=DEFAULT_FONT, font_size=34)
```

Update `shared/config.py` to include:
```python
DEFAULT_FONT = "Sans"
```

Every `Text(...)` call in scene files must include `font=DEFAULT_FONT`.
`MathTex(...)` is unaffected — LaTeX handles its own spacing.

---

## USING SLIDE IMAGES (SlideImage helper)

When a scene needs to show a diagram from the slides instead of a placeholder:

```python
# In scene file — load slide page 4 from the section's PDF
img = SlideImage(
    "../../content/01_diffusion_basics/slides.pdf",
    page=4,          # 1-indexed slide number
    width=3.5        # Manim display width
)
img.move_to(RIGHT*2 + DOWN*0.5)
self.play(FadeIn(img))
self.wait(1.0)

# To use only part of a slide (crop a diagram region):
img = SlideImage(
    "../../content/01_diffusion_basics/slides.pdf",
    page=4,
    width=3.5,
    crop=(0.05, 0.35, 0.50, 0.85)  # (x0, y0, x1, y1) in 0–1 fractions
    # this crops the left half, middle-to-bottom region
)
```

**When to use SlideImage vs drawing from scratch:**
- Use `SlideImage` when the slide has a complex diagram, photo, or figure
  that would take too long to recreate in Manim
- Draw from scratch when the visual is simple geometry (arrows, boxes, timelines)
- Never use SlideImage for text — re-create text as `Text()`/`MathTex()` instead

**Finding the right crop values:**
In SCRIPT.md, the action table can specify:
```
| 5 | fade_in | `diagram_img` | 1.0 | SlideImage(pdf, page=4, width=3.5, crop=(0.05,0.35,0.50,0.85)) · RIGHT*2 |
```

---

## OBJECT LIFECYCLE — preventing early/wrong-time appearances

Objects appearing too early or in wrong positions is caused by creating them
outside `construct()` or adding them to scene before their `self.play()` call.

**Rules:**

```python
# WRONG — obj created at top, appears immediately at scene start
class SceneN(Scene):
    def construct(self):
        obj = Text("hello")          # created but not played yet
        self.add(obj)                # THIS adds it instantly — WRONG
        self.wait(2)
        self.play(FadeIn(obj))       # too late, already visible

# CORRECT — only add objects via self.play()
class SceneN(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        obj = Text("hello", font=DEFAULT_FONT)
        # obj exists in memory but is NOT on screen yet
        self.wait(2)
        self.play(FadeIn(obj))       # appears exactly here

# WRONG — using self.add() for anything except background elements
self.add(obj)        # FORBIDDEN unless it's a static background

# CORRECT — every object enters via self.play()
self.play(FadeIn(obj),    run_time=1.0);  self.wait(0.5)
self.play(Write(eq),      run_time=2.0);  self.wait(1.0)
self.play(Create(arrow),  run_time=0.8);  self.wait(0.5)
```

**Overlap at wrong time — checklist:**
```
□ No self.add() calls except self.camera.background_color
□ Every object's first appearance is via self.play(FadeIn/Write/Create)
□ Objects being reused after FadeOut are re-created, not re-played
□ VGroup members are not individually added before the group is played
□ LaggedStart is used correctly — all targets exist before the call
```

**FadeOut everything at scene end:**
```python
# Always clean up — prevents bleed into next scene
self.play(FadeOut(*self.mobjects))
self.wait(2)
```

---

```markdown
---

## ARROW CONNECTIONS — ensuring arrows touch their targets

Arrows connecting two objects must have start/end points anchored to the
objects' boundaries. Never hardcode coordinates for arrow endpoints.

**Rules:**

```python
# WRONG — hardcoded positions, breaks if objects move or rescale
arrow = Arrow(LEFT * 2, RIGHT * 2)
arrow = Arrow(np.array([-2, 0, 0]), np.array([2, 0, 0]))

# WRONG — center-to-center, arrow floats inside both objects
arrow = Arrow(box_a.get_center(), box_b.get_center())

# CORRECT — derive endpoints from the objects themselves
arrow = Arrow(box_a.get_right(),  box_b.get_left())   # A → B horizontally
arrow = Arrow(box_a.get_bottom(), box_b.get_top())    # A → B vertically
arrow = Arrow(box_a.get_corner(UR), box_b.get_corner(DL))  # diagonal

# CORRECT — when direction is unknown at write time, compute it
direction = normalize(box_b.get_center() - box_a.get_center())
arrow = Arrow(
    box_a.get_boundary_point(direction),
    box_b.get_boundary_point(-direction),
    buff=0.1,
)
```

**buff — gap between arrowhead and object boundary:**
```python
Arrow(..., buff=0)    # flush, arrowhead touches object exactly
Arrow(..., buff=0.1)  # small breathing room (preferred)
# default buff=0.25 is often too large for tight diagrams
```

**Checklist before rendering any arrow:**
```
□ No hardcoded coordinates in start or end point
□ start uses a boundary method on the source object
□ end uses a boundary method on the target object
□ buff is set explicitly
□ Arrow still touches objects correctly if either is moved or rescaled
□ CurvedArrow follows the same rules — no hardcoded points
```

**Common patterns:**
```python
# Horizontal chain: A → B → C
Arrow(a.get_right(), b.get_left(), buff=0.1)
Arrow(b.get_right(), c.get_left(), buff=0.1)

# Vertical stack: A ↓ B
Arrow(a.get_bottom(), b.get_top(), buff=0.1)

# Curved arc between two objects
CurvedArrow(a.get_top(), b.get_top(), angle=-TAU/4)

# Labeled arrow — place label relative to arrow midpoint, not hardcoded
label = Text("label", font=DEFAULT_FONT, font_size=FONT_SMALL)
label.next_to(arrow.get_center(), UP, buff=0.15)
```
```

```markdown
---

## POSITIONING — anchor objects vs dependent objects

Hardcoded coordinates are only acceptable for **anchor objects** — the first
object placed to establish the layout of a scene. Everything else must be
positioned relative to something that already exists.

**Allowed — anchor placement:**
```python
# First object in a layout can use a hardcoded position to anchor the scene
box_a = Rectangle(width=2, height=1)
box_a.move_to(LEFT * 3)                       # OK — this is the layout anchor

box_b = Rectangle(width=2, height=1)
box_b.next_to(box_a, RIGHT, buff=1.0)         # depends on box_a — correct
```

**Forbidden — dependent objects must never hardcode:**
```python
# WRONG — caption hardcoded, breaks when its parent moves
caption.move_to(UP * 2.5)

# CORRECT — caption depends on what it describes
caption.next_to(arrow.get_center(), UP, buff=0.15)

# WRONG — label position duplicates its parent's coordinates
label.move_to(LEFT * 3 + DOWN * 1.2)

# CORRECT — label depends on the object it annotates
label.next_to(box_a, DOWN, buff=0.2)

# WRONG — arrow endpoints hardcoded
arrow = Arrow(LEFT * 2, RIGHT * 2)

# CORRECT — arrow endpoints derived from objects
arrow = Arrow(box_a.get_right(), box_b.get_left(), buff=0.1)
```

**Rule of thumb — dependency chain:**
```
anchor object      →  move_to(hardcoded)            ✓
child object       →  next_to(parent, DIR, buff)    ✓
grandchild         →  next_to(child,  DIR, buff)    ✓
label / caption / annotation  →  next_to(subject, DIR, buff)  ✓
arrow start / end  →  get_right() / get_left() / get_boundary_point()  ✓
```

**Checklist:**
```
□ Only anchor objects use move_to() with hardcoded values
□ Every other object uses next_to(), align_to(), or shift() relative to a parent
□ Arrow endpoints always use boundary methods — never hardcoded coords
□ Labels and captions use next_to() relative to the object they describe
□ Moving an anchor causes the entire sub-layout to follow correctly
□ No magic numbers duplicated across multiple objects in the same scene
```
```
