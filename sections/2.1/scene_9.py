from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
from config import *
from utils import *

class Scene9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        header = Text("VDM: Temporal Attention Layer", font=DEFAULT_FONT, font_size=40, color=WHITE)
        header.shift(UP * 3.0)
        idea = Text("Attend across time, not just space", font=DEFAULT_FONT, font_size=26, color=YELLOW)
        idea.shift(UP * 2.2)
        self.play(FadeIn(header), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(idea), run_time=0.6)
        self.wait(0.5)

        # ── Frame row with label to the left ─────────────
        frames_row = VGroup(*[
            Square(side_length=0.65, color=BLUE, fill_opacity=0.2)
            for _ in range(6)
        ])
        frames_row.arrange(RIGHT, buff=0.15)

        frame_lbl = Text("16 frames:", font=DEFAULT_FONT, font_size=22, color=WHITE)
        frame_lbl.next_to(frames_row, LEFT, buff=0.35)

        dots = Text("···", font=DEFAULT_FONT, font_size=28, color=WHITE)
        dots.next_to(frames_row, RIGHT, buff=0.2)

        row_group = VGroup(frame_lbl, frames_row, dots)
        row_group.move_to(UP * 0.2)
        if row_group.width > 11.5:
            row_group.scale_to_fit_width(11.5)

        self.play(FadeIn(frame_lbl), run_time=0.5)
        self.wait(0.5)
        self.play(Create(frames_row), run_time=1.0)
        self.wait(0.5)
        self.play(FadeIn(dots), run_time=0.4)
        self.wait(0.5)

        # ── Spatial attention arc ────────────────────────
        spattn_arc = CurvedArrow(
            frames_row[0].get_top() + UP * 0.05,
            frames_row[1].get_top() + UP * 0.05,
            angle=-TAU / 4, color=BLUE, stroke_width=2
        )
        spattn_lbl = Text("Spatial attn\n(within frame)", font=DEFAULT_FONT, font_size=20, color=BLUE)
        spattn_lbl.next_to(spattn_arc, UP, buff=0.15)
        self.play(Create(spattn_arc), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(spattn_lbl), run_time=0.5)
        self.wait(0.5)

        # ── Temporal attention arc ───────────────────────
        tattn_arc = CurvedArrow(
            frames_row[0].get_bottom() + DOWN * 0.05,
            frames_row[4].get_bottom() + DOWN * 0.05,
            angle=TAU / 4, color=GREEN, stroke_width=2
        )
        tattn_lbl = Text("Temporal attn\n(across frames per pixel)", font=DEFAULT_FONT, font_size=20, color=GREEN)
        tattn_lbl.next_to(tattn_arc, DOWN, buff=0.15)
        self.play(Create(tattn_arc), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(tattn_lbl), run_time=0.5)
        self.wait(5.0)

        key = Text(
            "Temporal attn: spatial axes as batch — each pixel attends across 16 time steps",
            font=DEFAULT_FONT, font_size=21, color=WHITE
        )
        key.shift(DOWN * 2.9)
        self.play(FadeIn(key), run_time=0.8)
        self.wait(5.0)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(2)
