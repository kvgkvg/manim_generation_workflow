from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
from config import *
from utils import *

class Scene11(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        header = Text("Make-A-Video: Cascaded Generation", font=DEFAULT_FONT, font_size=36, color=WHITE)
        header.shift(UP * 3.0)
        self.play(FadeIn(header), run_time=0.8)
        self.wait(0.5)

        stages = [
            ("ST Prior\n+ Decoder", BLUE,   -5.0),
            ("Frame\nInterp",       YELLOW,  -1.7),
            ("ST\nSuper-Res",       ORANGE,   1.6),
            ("Spatial\nSuper-Res",  RED,      4.9),
        ]
        out_labels = ["16fr\n64×64", "76fr\n64×64", "76fr\n256×256", "76fr\n768×768"]

        input_lbl = Text("Text\nPrompt", font=DEFAULT_FONT, font_size=20, color=WHITE)
        input_lbl.move_to(LEFT * 6.2 + UP * 0.5)
        self.play(FadeIn(input_lbl), run_time=0.5)
        self.wait(0.3)

        boxes = []
        for (label, color, x), out_text in zip(stages, out_labels):
            box = Rectangle(width=2.0, height=1.0, color=color, fill_opacity=0.25)
            box.move_to(RIGHT * x + UP * 0.5)
            lbl = Text(label, font=DEFAULT_FONT, font_size=17, color=color)
            lbl.move_to(box)
            out = Text(out_text, font=DEFAULT_FONT, font_size=15, color=WHITE)
            out.next_to(box, DOWN, buff=0.25)
            boxes.append((box, lbl, out))

        prev_obj = input_lbl
        for box, lbl, out in boxes:
            arr = Arrow(prev_obj.get_right(), box.get_left(),
                        color=WHITE, stroke_width=2, buff=0.05)
            self.play(FadeIn(arr), run_time=0.4)
            self.wait(0.3)
            self.play(Create(box), FadeIn(lbl), run_time=0.6)
            self.wait(0.3)
            self.play(FadeIn(out), run_time=0.4)
            self.wait(0.3)
            prev_obj = box

        self.wait(10.0)

        note = Text("4 stages: each trained on images first, then video",
                    font=DEFAULT_FONT, font_size=22, color=YELLOW)
        note.shift(DOWN * 3.0)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(5.0)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(2)
