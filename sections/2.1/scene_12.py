from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
from config import *
from utils import *

class Scene12(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        header = Text("Make-A-Video: Pseudo-3D Convolution", font=DEFAULT_FONT, font_size=36, color=WHITE)
        header.shift(UP * 3.0)
        paradigm = Text("Follows (2+1)D paradigm", font=DEFAULT_FONT, font_size=26, color=YELLOW)
        paradigm.shift(UP * 2.2)
        self.play(FadeIn(header), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(paradigm), run_time=0.6)
        self.wait(0.5)

        box_spatial = Rectangle(width=3.5, height=1.2, color=BLUE, fill_opacity=0.2)
        box_spatial.move_to(LEFT * 2.5 + UP * 0.8)
        lbl_sc = Text("Spatial 2D Conv\n(pretrained T2I weights)", font=DEFAULT_FONT, font_size=20, color=BLUE)
        lbl_sc.move_to(box_spatial)

        plus_c = Text("+", font=DEFAULT_FONT, font_size=36, color=WHITE)
        plus_c.move_to(UP * 0.8)

        box_temp = Rectangle(width=3.5, height=1.2, color=GREEN, fill_opacity=0.2)
        box_temp.move_to(RIGHT * 2.5 + UP * 0.8)
        lbl_tc = Text("Temporal 1D Conv\n(identity init)", font=DEFAULT_FONT, font_size=20, color=GREEN)
        lbl_tc.move_to(box_temp)

        self.play(Create(box_spatial), FadeIn(lbl_sc), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(plus_c), run_time=0.4)
        self.wait(0.3)
        self.play(Create(box_temp), FadeIn(lbl_tc), run_time=0.8)
        self.wait(0.5)

        init_detail = Text("Identity init:", font=DEFAULT_FONT, font_size=24, color=WHITE)
        init_detail.shift(DOWN * 0.5)
        self.play(FadeIn(init_detail), run_time=0.8)
        self.wait(0.5)

        init_eq = Text("0·f_prev  +  1·f_curr  +  0·f_next",
                       font=DEFAULT_FONT, font_size=26, color=GREEN)
        init_eq.shift(DOWN * 1.3)
        self.play(FadeIn(init_eq), run_time=1.0)
        self.wait(5.0)

        meaning = Text(
            "At init: temporal conv copies current frame\n(same as no temporal mixing)",
            font=DEFAULT_FONT, font_size=22, color=WHITE
        )
        meaning.shift(DOWN * 2.3)
        self.play(FadeIn(meaning), run_time=0.8)
        self.wait(8.0)

        self.play(Indicate(box_temp, color=YELLOW, scale_factor=1.08), run_time=0.8)
        self.wait(5.0)

        benefit = Text("Pretrained T2I intact → stable finetuning start",
                       font=DEFAULT_FONT, font_size=22, color=YELLOW)
        benefit.shift(DOWN * 3.1)
        self.play(FadeIn(benefit), run_time=0.6)
        self.wait(3.0)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(2)
