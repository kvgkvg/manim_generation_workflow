from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
from config import *
from utils import *

class Scene17(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        header = Text("Make-A-Video: Image Interpolation", font=DEFAULT_FONT, font_size=38, color=WHITE)
        header.shift(UP * 3.0)
        idea = Text("Given two images → generate in-between frames", font=DEFAULT_FONT, font_size=26, color=YELLOW)
        idea.shift(UP * 2.1)
        self.play(FadeIn(header), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(idea), run_time=0.6)
        self.wait(0.5)

        img_a = Rectangle(width=2.2, height=1.8, color=BLUE, fill_opacity=0.3)
        img_a.move_to(LEFT * 4.5)
        lbl_a = Text("Image A", font=DEFAULT_FONT, font_size=20, color=BLUE)
        lbl_a.next_to(img_a, DOWN, buff=0.2)
        self.play(Create(img_a), FadeIn(lbl_a), run_time=0.7)
        self.wait(0.5)

        mid_frames = VGroup(*[
            Rectangle(width=1.6, height=1.4, color=WHITE, fill_opacity=0.08, stroke_width=1)
            .move_to(LEFT * 1.8 + RIGHT * i * 1.2)
            for i in range(4)
        ])
        gen_lbl = Text("Generated frames", font=DEFAULT_FONT, font_size=17, color=WHITE)
        gen_lbl.set_opacity(0.7)
        gen_lbl.next_to(mid_frames, DOWN, buff=0.2)
        self.play(FadeIn(mid_frames), run_time=1.0)
        self.wait(0.5)
        self.play(FadeIn(gen_lbl), run_time=0.5)
        self.wait(0.5)

        img_b = Rectangle(width=2.2, height=1.8, color=GREEN, fill_opacity=0.3)
        img_b.move_to(RIGHT * 4.5)
        lbl_b = Text("Image B", font=DEFAULT_FONT, font_size=20, color=GREEN)
        lbl_b.next_to(img_b, DOWN, buff=0.2)
        self.play(Create(img_b), FadeIn(lbl_b), run_time=0.7)
        self.wait(5.0)

        note = Text(
            "Model learns motion and transitions\nbetween static images",
            font=DEFAULT_FONT, font_size=22, color=WHITE
        )
        note.shift(DOWN * 2.6)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(5.0)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(2)
