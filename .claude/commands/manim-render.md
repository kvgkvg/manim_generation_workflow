# Command: /manim-render
# Usage:
#   /manim-render <section> all              → render all scenes
#   /manim-render <section> scene 3          → render scene 3 only
#   /manim-render <section> scene 2 4 7      → render specific scenes
#   /manim-render <section> resume           → render unfinished only
#
# Example: /manim-render 01_diffusion_basics scene 3

---

## STEP 0 — Parse arguments

```bash
SECTION="$1"   # e.g. "01_diffusion_basics"
MODE="$2"      # "all" | "scene" | "resume"
# $3, $4 ... = scene numbers if MODE="scene"

if [ -z "$SECTION" ]; then
    echo "Usage: /manim-render <section> all|scene N|resume"
    echo "Available sections:"
    ls sections/ 2>/dev/null
    exit 1
fi

SCRIPT="sections/$SECTION/SCRIPT.md"
if [ ! -f "$SCRIPT" ]; then
    echo "ERROR: $SCRIPT not found. Run /manim-plan $SECTION first."
    exit 1
fi

echo "Section : $SECTION"
echo "Mode    : $MODE"
echo "Script  : $SCRIPT"
```

---

## STEP 1 — Bootstrap shared/ folder

Run once per project. Skip if already exists.

```bash
mkdir -p shared output

# shared/config.py
cat > shared/config.py << 'EOF'
BG_COLOR    = "#1C1C2E"
SQUARE_SIZE = 1.0;   SQUARE_GAP = 0.15
FONT_TITLE  = 48;    FONT_BODY  = 34
FONT_SMALL  = 24;    FONT_TINY  = 20
EOF

# shared/utils.py — NoisySquare with PIL (realistic noise)
cat > shared/utils.py << 'EOF'
from manim import *
from config import *
import numpy as np
from PIL import Image
import tempfile, os

def NoisySquare(t_ratio: float, size_px: int = 200) -> VGroup:
    base = Square(side_length=SQUARE_SIZE,
                  stroke_color=GRAY, stroke_width=1,
                  fill_color=BLACK, fill_opacity=1)
    if t_ratio == 0.0:
        base.set_fill(GREEN, opacity=0.85)
        return VGroup(base)

    rng = np.random.default_rng(seed=int(t_ratio * 1000))
    img = np.zeros((size_px, size_px, 3), dtype=np.float32)
    # Green fades to 0 as t_ratio → 1 (no color tint on pure noise)
    img[:, :, 1] = int(100 * (1 - t_ratio))

    noise = rng.normal(0, 255 * t_ratio, (size_px, size_px, 3))
    img = np.clip(img + noise, 0, 255).astype(np.uint8)

    tmp = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    Image.fromarray(img).save(tmp.name)
    img_mob = ImageMobject(tmp.name).set_width(SQUARE_SIZE)
    os.unlink(tmp.name)
    return VGroup(base, img_mob)

def NoiseTimeline(noise_ratios=None) -> VGroup:
    if noise_ratios is None:
        noise_ratios = [0, 0.15, 0.35, 0.55, 0.70, 0.85, 1.0]
    labels = [r"x_0",r"x_1",r"x_2",r"x_3",r"\ldots",r"x_t",r"\ldots",r"x_T"]
    g = VGroup()
    for i, ratio in enumerate(noise_ratios):
        sq = NoisySquare(ratio)
        lb = MathTex(labels[i], font_size=22).next_to(sq, DOWN, buff=0.2)
        g.add(VGroup(sq, lb))
    g.arrange(RIGHT, buff=SQUARE_GAP)
    if g.width > 11.0:
        g.scale_to_fit_width(11.0)
    return g

def NetworkBlock(label: str) -> VGroup:
    lt = Polygon([-1,.6,0],[-1,-.6,0],[0,0,0],
                 fill_color=BLUE, fill_opacity=0.8, stroke_width=0)
    rt = Polygon([1,.6,0],[1,-.6,0],[0,0,0],
                 fill_color=BLUE, fill_opacity=0.8, stroke_width=0)
    txt = Text(label, font_size=18, color=WHITE).move_to(ORIGIN)
    return VGroup(lt, rt, txt)

def make_summary_box(title, lines, title_color, box_color,
                     width=3.5, height=2.6) -> VGroup:
    rect = Rectangle(width=width, height=height, color=box_color,
                     stroke_width=2, fill_color=BLACK, fill_opacity=0.3)
    title_txt = Text(title, font_size=26, color=title_color)
    body = VGroup(*[Text(l, font_size=18, color=WHITE) for l in lines])
    body.arrange(DOWN, buff=0.18)
    content = VGroup(title_txt, body).arrange(DOWN, buff=0.22)
    if content.height > height - 0.4:
        content.scale_to_fit_height(height - 0.4)
    if content.width > width - 0.2:
        content.scale_to_fit_width(width - 0.2)
    content.move_to(rect.get_center())
    return VGroup(rect, content)
EOF

python3 -c "
import sys; sys.path.insert(0,'shared')
from utils import NoisySquare, NoiseTimeline, NetworkBlock
print('shared/utils.py OK')
"
```

---

## STEP 2 — Determine which scenes to render

```bash
python3 - << EOF
import re, os, sys

section  = "$SECTION"
mode     = "$MODE"
scene_args = "$@"  # remaining args after section + mode

script_path = f"sections/{section}/SCRIPT.md"
content = open(script_path).read()

# Find all scenes in SCRIPT.md
all_scenes = []
for m in re.finditer(r'^## SCENE (\d+)', content, re.MULTILINE):
    n = int(m.group(1))
    all_scenes.append(n)

print(f"Scenes in SCRIPT.md: {all_scenes}")

# Determine target scenes
if mode == "all":
    targets = all_scenes

elif mode == "resume":
    section_dir = f"sections/{section}"
    targets = []
    for n in all_scenes:
        py_file = f"{section_dir}/scene_{n}.py"
        if not os.path.exists(py_file):
            targets.append(n)
            continue
        # Try rendering to check if it works
        import subprocess
        r = subprocess.run(
            ["manim", "-pql", py_file, f"Scene{n}"],
            capture_output=True, cwd=section_dir
        )
        if r.returncode != 0:
            targets.append(n)
    print(f"Resume: rendering unfinished scenes: {targets}")

elif mode == "scene":
    nums = [int(x) for x in re.findall(r'\d+', scene_args)]
    targets = [n for n in nums if n in all_scenes]
    invalid = [n for n in nums if n not in all_scenes]
    if invalid:
        print(f"WARNING: Scenes {invalid} not found in SCRIPT.md — skipping")

else:
    targets = all_scenes

print(f"Will render: {targets}")

# Write targets to temp file for bash to read
with open("/tmp/render_targets.txt", "w") as f:
    f.write(" ".join(str(n) for n in targets))
EOF

TARGETS=$(cat /tmp/render_targets.txt)
echo "Targets: $TARGETS"
```

---

## STEP 3 — Per-scene render loop

For each scene number N in TARGETS:

### 3a. Generate scene_N.py

Read the action table for Scene N from `sections/$SECTION/SCRIPT.md`.

Implement as Python using this template:

```python
# sections/{SECTION}/scene_N.py
from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
from config import *
from utils import *

class SceneN(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── Step 1: [description] ─────────────────────────
        obj = ...
        self.play(FadeIn(obj), run_time=1.0)
        self.wait(1.0)

        # ── Step 2 ────────────────────────────────────────
        ...

        # ── End ───────────────────────────────────────────
        self.play(FadeOut(*self.mobjects))
        self.wait(2)
```

Write to `sections/$SECTION/scene_N.py`.

### 3b. Render

```bash
cd sections/$SECTION
manim -pql scene_N.py SceneN
echo "Exit: $?"
cd ../..
```

### 3c. Self-verify checklist

```
□ Exit code 0
□ All action rows from SCRIPT.md implemented in order
□ NoisySquare used for all noise visuals (no fill_color=WHITE)
□ No object referenced after FadeOut
□ Every self.play() followed by self.wait() ≥ 0.5s
□ MathTex uses r"..." prefix
□ No hex colors, no CYAN
□ No forbidden APIs
□ construct() ends with self.wait(2)
□ Duration within ±3s of target
□ No layout overflow x:[-6.5,6.5] y:[-3.5,3.5]
```

If any box fails → fix → re-render → re-check. Do not move to next scene.

### 3d. Register scene

```bash
python3 - << EOF
import os, re

section = "$SECTION"
n = N  # current scene number
registry = f"sections/{section}/render_registry.txt"

# Get duration from SCRIPT.md
content = open(f"sections/{section}/SCRIPT.md").read()
dur_match = re.search(rf'## SCENE {n}.*?\*\*Target:\*\*\s*(\d+)s', content, re.DOTALL)
duration = dur_match.group(1) if dur_match else "?"

entry = f"scene_{n}|Scene{n}|{duration}|{section}"
existing = open(registry).read() if os.path.exists(registry) else ""
if f"scene_{n}|" not in existing:
    with open(registry, "a") as f:
        f.write(entry + "\n")
    print(f"Registered: {entry}")
else:
    print(f"Already registered: scene_{n}")
EOF
```

### 3e. Report

```
✓ scene_N — Scene N: [Title]
  File    : sections/{SECTION}/scene_N.py
  Preview : media/videos/.../SceneN.mp4
  Duration: ~Xs (target: Xs)
```

---

## STEP 4 — Final summary

```
═══════════════════════════════════════════════════
  Render Complete — {SECTION}
═══════════════════════════════════════════════════
  ✓ scene_1   5s
  ✓ scene_2   40s
  ✗ scene_3   FAILED
  ✓ scene_4   45s
  ...
  Passed : N/Total
  Failed : M/Total

Next:
  /manim-render {SECTION} scene 3   → retry failed
  /manim-compose {SECTION}          → assemble section
  /manim-compose all                → assemble full video
═══════════════════════════════════════════════════
```
