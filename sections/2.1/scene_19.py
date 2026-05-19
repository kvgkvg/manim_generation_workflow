from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
from config import *
from utils import *

class Scene19(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        header = Text("Align your Latents", font=DEFAULT_FONT, font_size=48, color=WHITE)
        header.shift(UP * 2.8)
        org = Text("Blattmann et al., Nvidia — CVPR 2023", font=DEFAULT_FONT, font_size=22, color=WHITE)
        org.set_opacity(0.7)
        org.shift(UP * 2.1)
        self.play(FadeIn(header), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(org), run_time=0.5)
        self.wait(0.5)

        key_diff = Text("Key difference: operate in LATENT space", font=DEFAULT_FONT, font_size=28, color=YELLOW)
        key_diff.shift(UP * 1.3)
        self.play(FadeIn(key_diff), run_time=0.8)
        self.wait(0.5)

        box_pixel = Rectangle(width=3.2, height=0.9, color=RED, fill_opacity=0.2)
        box_pixel.move_to(LEFT * 2.5 + UP * 0.2)
        lbl_pspace = Text("Pixel space diffusion\n(Make-A-Video, VDM)", font=DEFAULT_FONT, font_size=19, color=RED)
        lbl_pspace.move_to(box_pixel)

        vs = Text("vs", font=DEFAULT_FONT, font_size=30, color=WHITE)
        vs.move_to(UP * 0.2)

        box_latent = Rectangle(width=3.2, height=0.9, color=GREEN, fill_opacity=0.2)
        box_latent.move_to(RIGHT * 2.5 + UP * 0.2)
        lbl_lspace = Text("Latent space diffusion\n(Align your Latents)", font=DEFAULT_FONT, font_size=19, color=GREEN)
        lbl_lspace.move_to(box_latent)

        self.play(Create(box_pixel), FadeIn(lbl_pspace), run_time=0.7)
        self.wait(0.5)
        self.play(FadeIn(vs), run_time=0.4)
        self.wait(0.3)
        self.play(Create(box_latent), FadeIn(lbl_lspace), run_time=0.7)
        self.wait(0.5)

        benefit_lbl = Text("Latent space benefits:", font=DEFAULT_FONT, font_size=24, color=WHITE)
        benefit_lbl.shift(DOWN * 0.9)
        b1 = Text("• Much smaller representation → faster training & inference",
                  font=DEFAULT_FONT, font_size=22, color=WHITE)
        b1.shift(DOWN * 1.5)
        b2 = Text("• Leverages Stable Diffusion pretrained weights directly",
                  font=DEFAULT_FONT, font_size=22, color=WHITE)
        b2.shift(DOWN * 2.1)

        self.play(FadeIn(benefit_lbl), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(b1), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(b2), run_time=0.5)
        self.wait(8.0)

        self.play(Indicate(box_latent, color=YELLOW, scale_factor=1.1), run_time=0.8)
        self.wait(4.0)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(2)
