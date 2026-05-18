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
BG_COLOR    = "#1C1C2E"
SQUARE_SIZE = 1.0;   SQUARE_GAP = 0.15
FONT_TITLE  = 48;    FONT_BODY  = 34
FONT_SMALL  = 24;    FONT_TINY  = 20
```

---

## Hard rules for every scene file

| Rule | Requirement |
|---|---|
| Imports | `from manim import *` then `import sys, os; sys.path.insert(0, "../../shared"); from config import *; from utils import *` |
| Colors | Built-in names only · no hex · no CYAN |
| MathTex | Always `r"..."` raw strings |
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
