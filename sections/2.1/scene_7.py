from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
from config import *
from utils import *

class Scene7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        header = Text("First Video Diffusion Model", font=DEFAULT_FONT, font_size=42, color=WHITE)
        header.shift(UP * 3.0)
        ref = Text("Ho et al. — NeurIPS 2022", font=DEFAULT_FONT, font_size=22, color=BLUE)
        ref.shift(UP * 2.3)
        milestone = Text("First diffusion model for video generation",
                         font=DEFAULT_FONT, font_size=28, color=YELLOW)
        milestone.shift(UP * 1.5)

        self.play(FadeIn(header), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(ref), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(milestone), run_time=0.8)
        self.wait(0.5)

        sq_noise = NoisySquare(1.0)
        sq_mid   = NoisySquare(0.5)
        sq_clean = NoisySquare(0.0)
        sq_noise.scale(0.9).move_to(LEFT * 4.0)
        sq_mid.scale(0.9).move_to(ORIGIN)
        sq_clean.scale(0.9).move_to(RIGHT * 4.0)

        arr1 = Arrow(LEFT * 2.8, LEFT * 0.7, color=WHITE, stroke_width=3)
        arr2 = Arrow(RIGHT * 0.7, RIGHT * 2.8, color=WHITE, stroke_width=3)

        lbl_noise = Text("Noise", font=DEFAULT_FONT, font_size=22, color=WHITE)
        lbl_noise.next_to(sq_noise, DOWN, buff=0.3)
        lbl_denoise = Text("Denoise", font=DEFAULT_FONT, font_size=22, color=WHITE)
        lbl_denoise.next_to(sq_mid, DOWN, buff=0.3)
        lbl_vid = Text("Video", font=DEFAULT_FONT, font_size=22, color=GREEN)
        lbl_vid.next_to(sq_clean, DOWN, buff=0.3)

        self.play(FadeIn(sq_noise), FadeIn(lbl_noise), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(arr1), run_time=0.4)
        self.wait(0.3)
        self.play(FadeIn(sq_mid), FadeIn(lbl_denoise), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(arr2), run_time=0.4)
        self.wait(0.3)
        self.play(FadeIn(sq_clean), FadeIn(lbl_vid), run_time=0.8)
        self.wait(0.5)

        spec = Text("16-frame videos · 64×64 resolution", font=DEFAULT_FONT, font_size=24, color=WHITE)
        spec.shift(DOWN * 2.5)
        self.play(FadeIn(spec), run_time=0.8)
        self.wait(8.0)

        key = Text("Key: extend 2D U-Net to 3D over space AND time",
                   font=DEFAULT_FONT, font_size=22, color=BLUE)
        key.shift(DOWN * 3.1)
        self.play(FadeIn(key), run_time=0.6)
        self.wait(4.0)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(2)
