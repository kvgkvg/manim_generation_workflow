from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
from config import *
from utils import *

class Scene18(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        title = Text("Imagen Video", font=DEFAULT_FONT, font_size=48, color=WHITE)
        title.shift(UP * 2.5)
        org = Text("Ho et al., Google — arXiv 2022", font=DEFAULT_FONT, font_size=22, color=WHITE)
        org.set_opacity(0.7)
        org.shift(UP * 1.7)
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(org), run_time=0.5)
        self.wait(0.5)

        similarity = Text("Similar to Make-A-Video:", font=DEFAULT_FONT, font_size=26, color=YELLOW)
        similarity.shift(UP * 0.7)
        self.play(FadeIn(similarity), run_time=0.8)
        self.wait(0.5)

        points = [
            "• Built on Imagen T2I foundation model",
            "• Cascaded generation pipeline",
            "• Temporal layers added to pretrained weights",
        ]
        for i, text in enumerate(points):
            pt = Text(text, font=DEFAULT_FONT, font_size=24, color=WHITE)
            pt.shift(UP * (0.0 - i * 0.6))
            self.play(FadeIn(pt), run_time=0.6)
            self.wait(0.5)

        self.wait(5.0)

        diff = Text(
            "Key difference: uses text diffusion prior (Imagen)\nnot CLIP embeddings",
            font=DEFAULT_FONT, font_size=22, color=BLUE
        )
        diff.shift(DOWN * 2.3)
        self.play(FadeIn(diff), run_time=0.8)
        self.wait(8.0)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(2)
