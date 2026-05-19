from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
from config import *
from utils import *

class Scene21(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        title = Text("Section 2.1 — Key Takeaways", font=DEFAULT_FONT, font_size=38, color=WHITE)
        title.shift(UP * 2.8)
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.5)

        takeaways = [
            ("1. T2V = extend T2I with temporal layers", BLUE),
            ("2. (2+1)D conv: efficient spatial+temporal factorization", GREEN),
            ("3. Cascaded pipelines: coarse → fine generation", YELLOW),
            ("4. Identity/zero init: stable finetuning from T2I", ORANGE),
            ("5. Latent space (Align your Latents) = faster + efficient", WHITE),
        ]
        y_positions = [1.5, 0.7, -0.1, -0.9, -1.7]

        for (text, color), y in zip(takeaways, y_positions):
            t = Text(text, font=DEFAULT_FONT, font_size=24, color=color)
            t.shift(UP * y)
            self.play(FadeIn(t), run_time=0.5)
            self.wait(0.3)

        self.wait(5.0)

        self.play(FadeOut(*self.mobjects), run_time=2.0)
        self.wait(2)
