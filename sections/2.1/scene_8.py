from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
from config import *
from utils import *

class Scene8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        header = Text("VDM Architecture: 3D U-Net", font=DEFAULT_FONT, font_size=40, color=WHITE)
        header.shift(UP * 3.0)
        idea_lbl = Text("Inflate 2D conv → space-only 3D conv", font=DEFAULT_FONT, font_size=28, color=YELLOW)
        idea_lbl.shift(UP * 2.1)
        self.play(FadeIn(header), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(idea_lbl), run_time=0.6)
        self.wait(0.5)

        box_2d = Rectangle(width=3.2, height=0.8, color=BLUE, fill_opacity=0.2)
        box_2d.move_to(LEFT * 2.8 + UP * 0.8)
        lbl_2d_k = Text("2D Conv:  3 × 3", font=DEFAULT_FONT, font_size=24, color=BLUE)
        lbl_2d_k.move_to(box_2d)
        self.play(Create(box_2d), FadeIn(lbl_2d_k), run_time=0.8)
        self.wait(0.5)

        box_3d = Rectangle(width=3.4, height=0.8, color=GREEN, fill_opacity=0.2)
        box_3d.move_to(RIGHT * 2.8 + UP * 0.8)
        lbl_3d_k = Text("3D Conv:  1 × 3 × 3", font=DEFAULT_FONT, font_size=24, color=GREEN)
        lbl_3d_k.move_to(box_3d)

        arr_inflate = Arrow(box_2d.get_right(), box_3d.get_left(),
                            color=WHITE, stroke_width=3, buff=0.05)
        infl_lbl = Text("inflate", font=DEFAULT_FONT, font_size=20, color=WHITE)
        infl_lbl.next_to(arr_inflate, UP, buff=0.15)
        self.play(FadeIn(arr_inflate), FadeIn(infl_lbl), run_time=0.5)
        self.wait(0.3)
        self.play(Create(box_3d), FadeIn(lbl_3d_k), run_time=0.8)
        self.wait(0.5)

        note1 = Text("Kernel size 1 along time dim → space-only",
                     font=DEFAULT_FONT, font_size=22, color=WHITE)
        note1.shift(DOWN * 0.3)
        self.play(FadeIn(note1), run_time=0.8)
        self.wait(0.5)

        feat_2d = Text("H × W × C", font=DEFAULT_FONT, font_size=26, color=BLUE)
        feat_2d.shift(DOWN * 1.2)
        self.play(FadeIn(feat_2d), run_time=0.6)
        self.wait(0.5)

        feat_3d = Text("T × H × W × C", font=DEFAULT_FONT, font_size=26, color=GREEN)
        feat_3d.shift(DOWN * 2.0)
        arr_feat = Arrow(feat_2d.get_bottom(), feat_3d.get_top(),
                         color=WHITE, stroke_width=2, buff=0.05)
        self.play(FadeIn(arr_feat), run_time=0.4)
        self.wait(0.3)
        self.play(FadeIn(feat_3d), run_time=0.6)
        self.wait(8.0)

        self.play(Indicate(box_3d, color=YELLOW, scale_factor=1.1), run_time=0.8)
        self.wait(4.0)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(2)
