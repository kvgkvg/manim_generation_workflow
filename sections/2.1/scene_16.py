from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
from config import *
from utils import *

class Scene16(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        header = Text("Make-A-Video: Evaluation", font=DEFAULT_FONT, font_size=44, color=WHITE)
        header.shift(UP * 3.0)
        self.play(FadeIn(header), run_time=0.8)
        self.wait(0.5)

        metrics_lbl = Text("Key metrics:", font=DEFAULT_FONT, font_size=28, color=YELLOW)
        metrics_lbl.shift(UP * 2.0)
        self.play(FadeIn(metrics_lbl), run_time=0.6)
        self.wait(0.5)

        box_fvd = Rectangle(width=3.0, height=0.9, color=BLUE, fill_opacity=0.2)
        box_fvd.move_to(LEFT * 2.8 + UP * 1.0)
        lbl_fvd = Text("FVD\n(video quality)", font=DEFAULT_FONT, font_size=20, color=BLUE)
        lbl_fvd.move_to(box_fvd)

        box_clip = Rectangle(width=3.0, height=0.9, color=GREEN, fill_opacity=0.2)
        box_clip.move_to(RIGHT * 2.8 + UP * 1.0)
        lbl_clip_s = Text("CLIP Similarity\n(text-video align)", font=DEFAULT_FONT, font_size=20, color=GREEN)
        lbl_clip_s.move_to(box_clip)
        self.play(Create(box_fvd), FadeIn(lbl_fvd), Create(box_clip), FadeIn(lbl_clip_s), run_time=0.8)
        self.wait(0.5)

        # Simple bar chart — FVD (lower=better), CLIP (higher=better)
        bar_prev_fvd = Rectangle(width=0.7, height=2.0, color=GRAY, fill_opacity=0.6)
        bar_mav_fvd  = Rectangle(width=0.7, height=1.1, color=BLUE, fill_opacity=0.8)
        bar_prev_fvd.move_to(LEFT * 2.5 + DOWN * 0.1)
        bar_mav_fvd.move_to(LEFT * 1.5 + DOWN * 0.55)

        lbl_prev  = Text("Prev\nSOTA", font=DEFAULT_FONT, font_size=13, color=GRAY)
        lbl_prev.next_to(bar_prev_fvd, DOWN, buff=0.1)
        lbl_mav_f = Text("MAV", font=DEFAULT_FONT, font_size=13, color=BLUE)
        lbl_mav_f.next_to(bar_mav_fvd, DOWN, buff=0.1)
        fvd_axis = Text("FVD ↓", font=DEFAULT_FONT, font_size=16, color=WHITE)
        fvd_axis.next_to(VGroup(bar_prev_fvd, bar_mav_fvd), LEFT, buff=0.3)

        bar_prev_clip = Rectangle(width=0.7, height=1.0, color=GRAY, fill_opacity=0.6)
        bar_mav_clip  = Rectangle(width=0.7, height=1.7, color=GREEN, fill_opacity=0.8)
        bar_prev_clip.move_to(RIGHT * 1.5 + DOWN * 0.6)
        bar_mav_clip.move_to(RIGHT * 2.5 + DOWN * 0.25)

        lbl_prev2 = Text("Prev\nSOTA", font=DEFAULT_FONT, font_size=13, color=GRAY)
        lbl_prev2.next_to(bar_prev_clip, DOWN, buff=0.1)
        lbl_mav_c = Text("MAV", font=DEFAULT_FONT, font_size=13, color=GREEN)
        lbl_mav_c.next_to(bar_mav_clip, DOWN, buff=0.1)
        clip_axis = Text("CLIP ↑", font=DEFAULT_FONT, font_size=16, color=WHITE)
        clip_axis.next_to(VGroup(bar_prev_clip, bar_mav_clip), RIGHT, buff=0.3)

        bars = VGroup(bar_prev_fvd, bar_mav_fvd, lbl_prev, lbl_mav_f, fvd_axis,
                      bar_prev_clip, bar_mav_clip, lbl_prev2, lbl_mav_c, clip_axis)
        self.play(FadeIn(bars), run_time=1.2)
        self.wait(5.0)

        human_note = Text(
            "Human evaluation: preferred Make-A-Video\nover previous models in quality & alignment",
            font=DEFAULT_FONT, font_size=22, color=WHITE
        )
        human_note.shift(DOWN * 2.8)
        self.play(FadeIn(human_note), run_time=0.8)
        self.wait(5.0)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(2)
