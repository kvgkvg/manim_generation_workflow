# Command: /manim-compose
# Usage:
#   /manim-compose <section>       → assemble one section → output/<section>.mp4
#   /manim-compose all             → assemble all sections → output/final_output.mp4
#   /manim-compose <section> hq    → re-render at 1080p then assemble
#   /manim-compose all hq          → re-render everything at 1080p then assemble

---

## STEP 0 — Parse arguments

```bash
TARGET="$1"    # section name OR "all"
HQ="$2"        # "hq" or empty

echo "Target : $TARGET"
echo "Quality: ${HQ:-normal (480p)}"
```

---

## STEP 1 — Validate

```bash
python3 - << EOF
import os, sys, glob

target = "$TARGET"

if target == "all":
    sections = sorted(glob.glob("sections/*/render_registry.txt"))
    sections = [os.path.dirname(s).replace("sections/","") for s in sections]
    if not sections:
        print("ERROR: No sections with render_registry.txt found.")
        print("Run /manim-render <section> first.")
        sys.exit(1)
    print(f"Sections to compose: {sections}")
else:
    reg = f"sections/{target}/render_registry.txt"
    if not os.path.exists(reg):
        print(f"ERROR: {reg} not found.")
        print(f"Run /manim-render {target} first.")
        sys.exit(1)
    print(f"Section: {target}")
EOF
```

---

## STEP 2 — Optional: re-render at 1080p (hq mode)

Only if `hq` flag passed:

```bash
python3 - << EOF
import subprocess, os, glob

target = "$TARGET"

if target == "all":
    regs = sorted(glob.glob("sections/*/render_registry.txt"))
    sections = [os.path.dirname(r).replace("sections/","") for r in regs]
else:
    sections = [target]

for section in sections:
    reg = f"sections/{section}/render_registry.txt"
    lines = [l.strip() for l in open(reg) if l.strip()]
    for line in lines:
        sf, cls = line.split("|")[0], line.split("|")[1]
        py_file = f"scene_{sf.split('_')[1]}.py"
        print(f"=== Re-rendering {cls} at 1080p ===")
        r = subprocess.run(
            ["manim", "-qh", py_file, cls],
            capture_output=True, text=True,
            cwd=f"sections/{section}"
        )
        status = "✓" if r.returncode == 0 else "✗"
        print(f"{status} {cls}")
        if r.returncode != 0:
            print(r.stderr[-200:])
EOF
```

---

## STEP 3 — Find mp4 files for each section

```bash
python3 - << EOF
import os, glob

def find_mp4(section, cls):
    """Search quality folders in priority order."""
    n = cls.replace("Scene","")
    for q in ["1080p60", "1080p30", "720p30", "480p15"]:
        path = f"media/videos/{section}/scene_{n}/{q}/{cls}.mp4"
        if os.path.exists(path):
            return os.path.abspath(path), q
    return None, None

target = "$TARGET"

if target == "all":
    regs = sorted(glob.glob("sections/*/render_registry.txt"))
    sections = [os.path.dirname(r).replace("sections/","") for r in regs]
else:
    sections = [target]

all_found = []
all_missing = []

for section in sections:
    lines = [l.strip() for l in open(f"sections/{section}/render_registry.txt") if l.strip()]
    for line in lines:
        parts = line.split("|")
        sf, cls = parts[0], parts[1]
        path, quality = find_mp4(section, cls)
        if path:
            all_found.append((section, cls, path, quality))
            print(f"✓ {section}/{cls} [{quality}]")
        else:
            all_missing.append(f"{section}/{cls}")
            print(f"✗ {section}/{cls} NOT FOUND")

if all_missing:
    print(f"\nMissing: {all_missing}")
    print("These scenes will be skipped in the output.")
EOF
```

---

## STEP 4 — Build file_list and compose

```bash
python3 - << EOF
import os, glob, subprocess

target = "$TARGET"
mkdir_p = lambda p: os.makedirs(p, exist_ok=True)
mkdir_p("output")

def find_mp4(section, cls):
    n = cls.replace("Scene","")
    for q in ["1080p60","1080p30","720p30","480p15"]:
        p = f"media/videos/{section}/scene_{n}/{q}/{cls}.mp4"
        if os.path.exists(p):
            return os.path.abspath(p)
    return None

def compose_section(section, out_file):
    reg = f"sections/{section}/render_registry.txt"
    if not os.path.exists(reg):
        print(f"SKIP: {section} — no registry")
        return False

    lines = [l.strip() for l in open(reg) if l.strip()]
    list_file = f"output/file_list_{section}.txt"
    count = 0
    with open(list_file, "w") as f:
        for line in lines:
            parts = line.split("|")
            sf, cls = parts[0], parts[1]
            path = find_mp4(section, cls)
            if path:
                f.write(f"file '{path}'\n")
                count += 1

    if count == 0:
        print(f"SKIP: {section} — no rendered scenes found")
        return False

    r = subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0",
         "-i", list_file, "-c", "copy", out_file],
        capture_output=True, text=True
    )
    if r.returncode == 0:
        size = os.path.getsize(out_file) / 1024 / 1024
        print(f"✓ {out_file} ({size:.1f} MB, {count} scenes)")
        return True
    else:
        print(f"✗ {out_file} FAILED: {r.stderr[-200:]}")
        return False

if target == "all":
    regs = sorted(glob.glob("sections/*/render_registry.txt"))
    sections = [os.path.dirname(r).replace("sections/","") for r in regs]

    # Compose each section individually
    section_files = []
    for section in sections:
        out = f"output/{section}.mp4"
        if compose_section(section, out):
            section_files.append(out)

    # Compose all sections into final video
    if len(section_files) > 1:
        master_list = "output/file_list_all.txt"
        with open(master_list, "w") as f:
            for sf in section_files:
                f.write(f"file '{os.path.abspath(sf)}'\n")
        r = subprocess.run(
            ["ffmpeg", "-y", "-f", "concat", "-safe", "0",
             "-i", master_list, "-c", "copy", "output/final_output.mp4"],
            capture_output=True, text=True
        )
        if r.returncode == 0:
            size = os.path.getsize("output/final_output.mp4") / 1024 / 1024
            print(f"\n✓ output/final_output.mp4 ({size:.1f} MB)")
        else:
            print(f"\n✗ final_output.mp4 FAILED: {r.stderr[-200:]}")
    elif len(section_files) == 1:
        import shutil
        shutil.copy(section_files[0], "output/final_output.mp4")
        print(f"\n✓ output/final_output.mp4 (single section)")
else:
    out = f"output/{target}.mp4"
    compose_section(target, out)
EOF
```

---

## STEP 5 — Verify and report

```bash
python3 - << EOF
import subprocess, os, glob

target = "$TARGET"
files = (glob.glob("output/*.mp4") if target == "all"
         else [f"output/{target}.mp4"])

print("\n" + "="*55)
print("  Compose Complete")
print("="*55)

for f in sorted(files):
    if not os.path.exists(f):
        continue
    r = subprocess.run(
        ["ffprobe", "-v","quiet",
         "-show_entries","format=duration",
         "-show_entries","stream=width,height,r_frame_rate",
         "-of","default=noprint_wrappers=1", f],
        capture_output=True, text=True
    )
    size = os.path.getsize(f) / 1024 / 1024
    print(f"\n  {f}")
    print(f"  Size    : {size:.1f} MB")
    for line in r.stdout.strip().splitlines():
        print(f"  {line}")

print("="*55)
EOF
```
