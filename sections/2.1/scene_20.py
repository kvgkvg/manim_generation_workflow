from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
from config import *
from utils import *

class Scene20(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        header = Text("Align your Latents: Architecture", font=DEFAULT_FONT, font_size=38, color=WHITE)
        header.shift(UP * 3.0)
        base = Text("Base: Stable Diffusion LDM", font=DEFAULT_FONT, font_size=26, color=YELLOW)
        base.shift(UP * 2.2)
        self.play(FadeIn(header), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(base), run_time=0.6)
        self.wait(0.5)

        box_ldm = Rectangle(width=3.2, height=1.2, color=BLUE, fill_opacity=0.2)
        box_ldm.move_to(LEFT * 2.8 + UP * 1.0)
        lbl_ldm = Text("Latent Diffusion\n+ Temporal Conv\n+ 3D Attention",
                       font=DEFAULT_FONT, font_size=17, color=BLUE)
        lbl_ldm.move_to(box_ldm)

        box_dec = Rectangle(width=3.2, height=1.2, color=GREEN, fill_opacity=0.2)
        box_dec.move_to(RIGHT * 2.8 + UP * 1.0)
        lbl_dec = Text("Decoder\n+ 3D Conv layers\n(temporal consistency)",
                       font=DEFAULT_FONT, font_size=17, color=GREEN)
        lbl_dec.move_to(box_dec)

        arr_flow = Arrow(box_ldm.get_right(), box_dec.get_left(),
                         color=WHITE, stroke_width=3, buff=0.05)
        self.play(Create(box_ldm), FadeIn(lbl_ldm), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(arr_flow), run_time=0.5)
        self.wait(0.3)
        self.play(Create(box_dec), FadeIn(lbl_dec), run_time=0.8)
        self.wait(0.5)

        box_up = Rectangle(width=3.5, height=0.8, color=ORANGE, fill_opacity=0.2)
        box_up.shift(DOWN * 0.3)
        lbl_up = Text("Upsampler + 3D Conv (spatial super-resolution)",
                      font=DEFAULT_FONT, font_size=19, color=ORANGE)
        lbl_up.move_to(box_up)
        self.play(Create(box_up), FadeIn(lbl_up), run_time=0.7)
        self.wait(5.0)

        compare = Text(
            "Same idea as Make-A-Video, but in compressed latent space\n→ more computationally efficient",
            font=DEFAULT_FONT, font_size=22, color=WHITE
        )
        compare.shift(DOWN * 1.7)
        self.play(FadeIn(compare), run_time=0.8)
        self.wait(8.0)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(2)
