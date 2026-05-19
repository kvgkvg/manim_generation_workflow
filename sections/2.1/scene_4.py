from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
from config import *
from utils import *

class Scene4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        header = Text("From 2D to 3D Output", font=DEFAULT_FONT, font_size=44, color=WHITE)
        header.shift(UP * 3.0)
        self.play(FadeIn(header), run_time=0.8)
        self.wait(0.5)

        single_frame = Rectangle(width=3.0, height=2.2, color=BLUE, fill_opacity=0.2)
        single_frame.move_to(LEFT * 3.5)
        lbl_2d = Text("2D Image", font=DEFAULT_FONT, font_size=26, color=BLUE)
        lbl_2d.next_to(single_frame, DOWN, buff=0.3)
        dim_lbl = Text("H × W × C", font=DEFAULT_FONT, font_size=22, color=WHITE)
        dim_lbl.move_to(single_frame)

        self.play(Create(single_frame), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(lbl_2d), FadeIn(dim_lbl), run_time=0.5)
        self.wait(0.5)

        arr_right = Arrow(LEFT * 1.0, RIGHT * 0.5, color=WHITE, stroke_width=3)
        x16_lbl = Text("×16 frames", font=DEFAULT_FONT, font_size=26, color=YELLOW)
        x16_lbl.next_to(arr_right, UP, buff=0.2)
        self.play(FadeIn(arr_right), FadeIn(x16_lbl), run_time=0.8)
        self.wait(0.5)

        frames = VGroup(*[
            Rectangle(width=2.4, height=1.8, color=GREEN, fill_opacity=0.12)
            .shift(RIGHT * (i * 0.2) + DOWN * (i * 0.18))
            for i in range(5)
        ])
        frames.move_to(RIGHT * 3.5)
        lbl_3d = Text("3D Video", font=DEFAULT_FONT, font_size=26, color=GREEN)
        lbl_3d.next_to(frames, DOWN, buff=0.3)
        dim_lbl_3d = Text("T × H × W × C", font=DEFAULT_FONT, font_size=22, color=WHITE)
        dim_lbl_3d.move_to(frames.get_center())

        self.play(Create(frames), run_time=1.2)
        self.wait(0.5)
        self.play(FadeIn(lbl_3d), FadeIn(dim_lbl_3d), run_time=0.5)
        self.wait(8.0)

        note = Text("New challenge: model must learn temporal coherence",
                    font=DEFAULT_FONT, font_size=24, color=YELLOW)
        note.shift(DOWN * 2.8)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(5.0)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(2)
