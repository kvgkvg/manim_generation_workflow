from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
from config import *
from utils import *

class Scene5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        header = Text("Handling Video: 3D Convolutions", font=DEFAULT_FONT, font_size=40, color=WHITE)
        header.shift(UP * 3.0)
        ref = Text("Tran et al., C3D — ICCV 2015", font=DEFAULT_FONT, font_size=18, color=WHITE)
        ref.set_opacity(0.6)
        ref.shift(UP * 2.4)
        self.play(FadeIn(header), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(ref), run_time=0.5)
        self.wait(0.5)

        lbl_2d_conv = Text("2D Conv", font=DEFAULT_FONT, font_size=30, color=BLUE)
        lbl_2d_conv.move_to(LEFT * 3.5 + UP * 1.2)
        self.play(FadeIn(lbl_2d_conv), run_time=0.6)
        self.wait(0.5)

        kernel_2d = VGroup(*[
            Square(side_length=0.55, color=BLUE, fill_opacity=0.3)
            .shift(RIGHT * (j * 0.58) + DOWN * (i * 0.58))
            for i in range(3) for j in range(3)
        ])
        kernel_2d.move_to(LEFT * 3.5 + DOWN * 0.2)
        size_2d = Text("3 × 3", font=DEFAULT_FONT, font_size=28, color=BLUE)
        size_2d.next_to(kernel_2d, DOWN, buff=0.3)

        self.play(Create(kernel_2d), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(size_2d), run_time=0.5)
        self.wait(0.5)

        arr_extend = Arrow(LEFT * 1.2, RIGHT * 0.8, color=WHITE, stroke_width=3)
        extend_lbl = Text("extend\nto time", font=DEFAULT_FONT, font_size=20, color=WHITE)
        extend_lbl.next_to(arr_extend, UP, buff=0.2)
        self.play(FadeIn(arr_extend), FadeIn(extend_lbl), run_time=0.8)
        self.wait(0.5)

        lbl_3d_conv = Text("3D Conv", font=DEFAULT_FONT, font_size=30, color=GREEN)
        lbl_3d_conv.move_to(RIGHT * 3.5 + UP * 1.2)
        self.play(FadeIn(lbl_3d_conv), run_time=0.6)
        self.wait(0.5)

        layers = VGroup()
        for k in range(3):
            layer = VGroup(*[
                Square(side_length=0.48, color=GREEN, fill_opacity=0.15 + k * 0.08)
                .shift(RIGHT * (j * 0.51) + DOWN * (i * 0.51))
                for i in range(3) for j in range(3)
            ])
            layer.shift(RIGHT * (k * 0.18) + DOWN * (k * 0.16))
            layers.add(layer)
        layers.move_to(RIGHT * 3.5 + DOWN * 0.2)
        size_3d = Text("3 × 3 × 3", font=DEFAULT_FONT, font_size=28, color=GREEN)
        size_3d.next_to(layers, DOWN, buff=0.3)

        self.play(Create(layers), run_time=1.0)
        self.wait(0.5)
        self.play(FadeIn(size_3d), run_time=0.5)
        self.wait(0.5)

        dim_note = Text("Spatial dims (H, W) + Temporal dim (T)",
                        font=DEFAULT_FONT, font_size=24, color=WHITE)
        dim_note.shift(DOWN * 2.5)
        self.play(FadeIn(dim_note), run_time=0.8)
        self.wait(8.0)

        cost_note = Text("Cost: 3× more parameters — expensive!",
                         font=DEFAULT_FONT, font_size=22, color=RED)
        cost_note.shift(DOWN * 3.1)
        self.play(FadeIn(cost_note), run_time=0.6)
        self.wait(5.0)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(2)
