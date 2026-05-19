from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
from config import *
from utils import *

class Scene1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        title = Text("Video Generation", font=DEFAULT_FONT, font_size=52, color=WHITE)
        title.shift(UP * 0.5)
        subtitle = Text("2.1 — Pioneering & Early Works", font=DEFAULT_FONT, font_size=32, color=BLUE)
        subtitle.next_to(title, DOWN, buff=0.4)
        credit = Text("CVPR 2024 Tutorial", font=DEFAULT_FONT, font_size=22, color=WHITE)
        credit.set_opacity(0.6)
        credit.next_to(subtitle, DOWN, buff=0.3)

        self.play(FadeIn(title), run_time=1.0)
        self.wait(0.5)
        self.play(FadeIn(subtitle), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(credit), run_time=0.5)
        self.wait(3.0)
        self.play(FadeOut(*self.mobjects), run_time=1.5)
        self.wait(2)
