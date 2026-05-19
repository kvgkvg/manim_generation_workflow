from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
from config import *
from utils import *

class Scene6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        header = Text("(2+1)D Convolutions", font=DEFAULT_FONT, font_size=44, color=WHITE)
        header.shift(UP * 3.0)
        ref = Text("Tran et al., CVPR 2018", font=DEFAULT_FONT, font_size=18, color=WHITE)
        ref.set_opacity(0.6)
        ref.shift(UP * 2.4)
        self.play(FadeIn(header), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(ref), run_time=0.5)
        self.wait(0.5)

        idea = Text("Factorize 3D conv into two steps:", font=DEFAULT_FONT, font_size=28, color=WHITE)
        idea.shift(UP * 1.6)
        self.play(FadeIn(idea), run_time=0.6)
        self.wait(0.5)

        box_spatial = Rectangle(width=3.2, height=1.0, color=BLUE, fill_opacity=0.2)
        box_spatial.move_to(LEFT * 2.5 + UP * 0.3)
        lbl_spatial = Text("2D Spatial Conv\n(H × W)", font=DEFAULT_FONT, font_size=22, color=BLUE)
        lbl_spatial.move_to(box_spatial)

        plus = Text("+", font=DEFAULT_FONT, font_size=40, color=WHITE)
        plus.move_to(UP * 0.3)

        box_temporal = Rectangle(width=3.2, height=1.0, color=GREEN, fill_opacity=0.2)
        box_temporal.move_to(RIGHT * 2.5 + UP * 0.3)
        lbl_temporal = Text("1D Temporal Conv\n(T)", font=DEFAULT_FONT, font_size=22, color=GREEN)
        lbl_temporal.move_to(box_temporal)

        self.play(Create(box_spatial), FadeIn(lbl_spatial), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(plus), run_time=0.4)
        self.wait(0.3)
        self.play(Create(box_temporal), FadeIn(lbl_temporal), run_time=0.8)
        self.wait(0.5)

        eq = Text("f(2+1)D  =  f_T  ∘  f_HW", font=DEFAULT_FONT, font_size=28, color=YELLOW)
        eq.shift(DOWN * 1.0)
        self.play(FadeIn(eq), run_time=1.0)
        self.wait(5.0)

        benefit = Text("Captures temporal dynamics with fewer parameters than full 3D conv",
                       font=DEFAULT_FONT, font_size=22, color=WHITE)
        benefit.shift(DOWN * 2.2)
        self.play(FadeIn(benefit), run_time=0.8)
        self.wait(8.0)

        self.play(Indicate(box_temporal, color=YELLOW, scale_factor=1.1), run_time=0.8)
        self.wait(3.0)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(2)
