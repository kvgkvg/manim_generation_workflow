#!/usr/bin/env bash
set -e

echo "=== Manim Workflow Setup ==="

# 1. Conda env
if conda env list | grep -q "^manim-workflow "; then
  echo "[skip] conda env 'manim-workflow' already exists"
else
  echo "[create] conda env from environment.yml..."
  conda env create -f environment.yml
fi

# 2. Activate hint (can't activate inside script, inform user)
echo ""
echo "=== Done ==="
echo "Activate with:  conda activate manim-workflow"
echo "Then verify:    manim --version"
echo ""
echo "NOTE: LaTeX must be installed separately (system package manager):"
echo "  Arch/Manjaro:  sudo pacman -S texlive-most"
echo "  Ubuntu/Debian: sudo apt install texlive-full"
echo "  macOS:         brew install --cask mactex"
