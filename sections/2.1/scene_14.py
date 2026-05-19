from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
from config import *
from utils import *

class Scene14(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        header = Text("Make-A-Video: Training Strategy", font=DEFAULT_FONT, font_size=40, color=WHITE)
        header.shift(UP * 3.0)
        sub = Text("4 networks, 2-phase training", font=DEFAULT_FONT, font_size=26, color=YELLOW)
        sub.shift(UP * 2.2)
        self.play(FadeIn(header), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(sub), run_time=0.5)
        self.wait(0.5)

        box1 = Rectangle(width=5.0, height=0.8, color=BLUE, fill_opacity=0.2)
        box1.move_to(UP * 1.2)
        lbl1 = Text("Phase 1: Train all 4 networks on image data",
                    font=DEFAULT_FONT, font_size=20, color=BLUE)
        lbl1.move_to(box1)
        self.play(Create(box1), FadeIn(lbl1), run_time=0.7)
        self.wait(0.5)

        arr12 = Arrow(box1.get_bottom(), DOWN * 0.0, color=WHITE, stroke_width=2, buff=0.05)
        self.play(FadeIn(arr12), run_time=0.4)
        self.wait(0.3)

        box2 = Rectangle(width=5.0, height=0.8, color=GREEN, fill_opacity=0.2)
        box2.move_to(DOWN * 0.3)
        lbl2 = Text("Phase 2: Insert temporal layers, finetune on video",
                    font=DEFAULT_FONT, font_size=20, color=GREEN)
        lbl2.move_to(box2)
        self.play(Create(box2), FadeIn(lbl2), run_time=0.7)
        self.wait(0.5)

        arr23 = Arrow(box2.get_bottom(), DOWN * 1.6, color=WHITE, stroke_width=2, buff=0.05)
        self.play(FadeIn(arr23), run_time=0.4)
        self.wait(0.3)

        box3 = Rectangle(width=5.0, height=0.8, color=ORANGE, fill_opacity=0.2)
        box3.move_to(DOWN * 1.9)
        lbl3 = Text("Data: WebVid-10M + 10M HD-VILA subset",
                    font=DEFAULT_FONT, font_size=20, color=ORANGE)
        lbl3.move_to(box3)
        self.play(Create(box3), FadeIn(lbl3), run_time=0.7)
        self.wait(8.0)

        note = Text(
            "Spatial weights frozen during video finetuning\n→ preserves image quality",
            font=DEFAULT_FONT, font_size=22, color=WHITE
        )
        note.shift(DOWN * 2.9)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(5.0)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(2)
