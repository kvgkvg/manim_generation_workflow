from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
from config import *
from utils import *

class Scene2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        header = Text("Video Generation Landscape", font=DEFAULT_FONT, font_size=40, color=WHITE)
        header.shift(UP * 3.0)
        self.play(FadeIn(header), run_time=0.8)
        self.wait(0.5)

        center_box = Rectangle(width=2.8, height=0.7, color=BLUE)
        center_box.shift(UP * 1.2)
        center_lbl = Text("Video Generation", font=DEFAULT_FONT, font_size=24, color=BLUE)
        center_lbl.move_to(center_box)
        self.play(Create(center_box), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(center_lbl), run_time=0.5)
        self.wait(0.3)

        # Create target boxes first so arrows can use their edges
        box_pixel = Rectangle(width=2.4, height=0.6, color=GREEN)
        box_pixel.move_to(LEFT * 4.5 + UP * 1.2)
        lbl_pixel = Text("Pixel Space", font=DEFAULT_FONT, font_size=22, color=GREEN)
        lbl_pixel.move_to(box_pixel)

        box_latent = Rectangle(width=2.4, height=0.6, color=YELLOW)
        box_latent.move_to(RIGHT * 4.5 + UP * 1.2)
        lbl_latent = Text("Latent Space", font=DEFAULT_FONT, font_size=22, color=YELLOW)
        lbl_latent.move_to(box_latent)

        box_cascade = Rectangle(width=2.4, height=0.6, color=ORANGE)
        box_cascade.move_to(UP * 0.2)
        lbl_cascade = Text("Cascaded", font=DEFAULT_FONT, font_size=22, color=ORANGE)
        lbl_cascade.move_to(box_cascade)

        arr_left = Arrow(center_box.get_left(), box_pixel.get_right(),
                         color=WHITE, stroke_width=2, buff=0.05)
        arr_right = Arrow(center_box.get_right(), box_latent.get_left(),
                          color=WHITE, stroke_width=2, buff=0.05)
        arr_down = Arrow(center_box.get_bottom(), box_cascade.get_top(),
                         color=WHITE, stroke_width=2, buff=0.05)
        self.play(Create(arr_left), Create(arr_right), Create(arr_down), run_time=0.5)
        self.wait(0.3)

        self.play(Create(box_pixel), FadeIn(lbl_pixel), run_time=0.6)
        self.wait(0.3)
        self.play(Create(box_latent), FadeIn(lbl_latent), run_time=0.6)
        self.wait(0.3)
        self.play(Create(box_cascade), FadeIn(lbl_cascade), run_time=0.6)
        self.wait(0.3)

        works_pixel = Text("VDM · Make-A-Video\nImagen Video", font=DEFAULT_FONT, font_size=18, color=WHITE)
        works_pixel.next_to(box_pixel, DOWN, buff=0.25)
        works_latent = Text("Align your Latents\nVideoCrafter", font=DEFAULT_FONT, font_size=18, color=WHITE)
        works_latent.next_to(box_latent, DOWN, buff=0.25)
        self.play(FadeIn(works_pixel), FadeIn(works_latent), run_time=0.8)
        self.wait(5.0)

        note = Text("Focus: pioneering works from 2022–2023", font=DEFAULT_FONT, font_size=22, color=BLUE)
        note.shift(DOWN * 2.8)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(5.0)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(2)
