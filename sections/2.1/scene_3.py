from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
from config import *
from utils import *

class Scene3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── Header ───────────────────────────────────────
        header = Text("Problem Definition", font=DEFAULT_FONT, font_size=44, color=WHITE)
        header.shift(UP * 3.0)
        self.play(FadeIn(header), run_time=0.8)
        self.wait(0.5)

        # ── Divider ──────────────────────────────────────
        divider = Line(UP * 2.5, DOWN * 2.5, color=WHITE, stroke_width=1)
        divider.set_opacity(0.4)
        self.play(Create(divider), run_time=0.5)
        self.wait(0.3)

        # ── Column labels ────────────────────────────────
        lbl_t2i = Text("Text-to-Image (T2I)", font=DEFAULT_FONT, font_size=28, color=BLUE)
        lbl_t2i.move_to(LEFT * 3.2 + UP * 2.0)
        lbl_t2v = Text("Text-to-Video (T2V)", font=DEFAULT_FONT, font_size=28, color=GREEN)
        lbl_t2v.move_to(RIGHT * 3.2 + UP * 2.0)
        self.play(FadeIn(lbl_t2i), FadeIn(lbl_t2v), run_time=0.6)
        self.wait(0.5)

        # ── Text prompt boxes ────────────────────────────
        text_box_i = Rectangle(width=3, height=0.7, color=BLUE)
        text_box_i.move_to(LEFT * 3.2 + UP * 1.0)
        text_lbl_i = Text('Prompt', font=DEFAULT_FONT, font_size=18, color=WHITE)
        text_lbl_i.move_to(text_box_i)

        text_box_v = Rectangle(width=3, height=0.7, color=GREEN)
        text_box_v.move_to(RIGHT * 3.2 + UP * 1.0)
        text_lbl_v = Text('Prompt', font=DEFAULT_FONT, font_size=18, color=WHITE)
        text_lbl_v.move_to(text_box_v)

        self.play(Create(text_box_i), FadeIn(text_lbl_i), run_time=0.8)
        self.wait(0.5)
        self.play(Create(text_box_v), FadeIn(text_lbl_v), run_time=0.8)
        self.wait(0.5)

        # ── Arrows down ──────────────────────────────────
        arr_i = Arrow(
            LEFT * 3.2 + UP * 0.55, LEFT * 3.2 + DOWN * 0.05,
            color=WHITE, stroke_width=3, buff=0.0
        )
        arr_v = Arrow(
            RIGHT * 3.2 + UP * 0.55, RIGHT * 3.2 + DOWN * 0.05,
            color=WHITE, stroke_width=3, buff=0.0
        )
        self.play(FadeIn(arr_i), FadeIn(arr_v), run_time=0.5)
        self.wait(0.3)

        # ── Output visuals ───────────────────────────────
        img_box = Rectangle(width=3.0, height=2.2, color=BLUE, fill_opacity=0.15)
        img_box.move_to(LEFT * 3.2 + DOWN * 1.4)
        img_lbl = Text("Image", font=DEFAULT_FONT, font_size=22, color=BLUE)
        img_lbl.move_to(img_box)
        self.play(Create(img_box), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(img_lbl), run_time=0.5)
        self.wait(0.3)

        # Stacked frames suggesting 3D video
        frames = VGroup(*[
            Rectangle(
                width=2.6, height=1.9, color=GREEN, fill_opacity=0.1
            ).shift(RIGHT * (i * 0.18) + DOWN * (i * 0.15))
            for i in range(4)
        ])
        frames.move_to(RIGHT * 3.2 + DOWN * 1.2)
        self.play(Create(frames), run_time=1.0)
        self.wait(0.3)

        vid_lbl = Text("Video\n(sequence of frames)", font=DEFAULT_FONT, font_size=20, color=GREEN)
        vid_lbl.next_to(frames, DOWN, buff=0.25)
        self.play(FadeIn(vid_lbl), run_time=0.5)
        self.wait(8.0)

        # ── Highlight T2V ────────────────────────────────
        self.play(Indicate(lbl_t2v, color=YELLOW, scale_factor=1.15), run_time=0.8)
        self.wait(3.0)

        # ── Fade out ─────────────────────────────────────
        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(2)
