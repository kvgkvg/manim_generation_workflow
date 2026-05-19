from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
from config import *
from utils import *

class Scene10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        title = Text("Make-A-Video", font=DEFAULT_FONT, font_size=52, color=ORANGE)
        title.shift(UP * 1.5)
        org = Text("Singer et al., Meta — arXiv 2022", font=DEFAULT_FONT, font_size=24, color=WHITE)
        org.set_opacity(0.7)
        org.shift(UP * 0.6)
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(org), run_time=0.5)
        self.wait(0.5)

        key_insight = Text("Key insight:", font=DEFAULT_FONT, font_size=30, color=YELLOW)
        key_insight.shift(DOWN * 0.3)
        self.play(FadeIn(key_insight), run_time=1.0)
        self.wait(0.5)

        insight_body = Text(
            "Generate videos without text-video training pairs!\nLeverage pretrained T2I knowledge.",
            font=DEFAULT_FONT, font_size=26, color=WHITE
        )
        insight_body.shift(DOWN * 1.2)
        self.play(FadeIn(insight_body), run_time=1.0)
        self.wait(5.0)

        box_t2i = Rectangle(width=3.0, height=0.8, color=BLUE, fill_opacity=0.2)
        box_t2i.move_to(LEFT * 2.5 + DOWN * 2.5)
        t2i_lbl = Text("T2I Model\n(pretrained)", font=DEFAULT_FONT, font_size=20, color=BLUE)
        t2i_lbl.move_to(box_t2i)

        box_t2v = Rectangle(width=3.0, height=0.8, color=ORANGE, fill_opacity=0.2)
        box_t2v.move_to(RIGHT * 2.5 + DOWN * 2.5)
        t2v_lbl = Text("T2V Model\n(+ temporal layers)", font=DEFAULT_FONT, font_size=20, color=ORANGE)
        t2v_lbl.move_to(box_t2v)

        arr_lift = Arrow(box_t2i.get_right(), box_t2v.get_left(),
                         color=WHITE, stroke_width=3, buff=0.05)
        self.play(Create(box_t2i), FadeIn(t2i_lbl), run_time=0.7)
        self.wait(0.5)
        self.play(FadeIn(arr_lift), run_time=0.5)
        self.wait(0.3)
        self.play(Create(box_t2v), FadeIn(t2v_lbl), run_time=0.7)
        self.wait(5.0)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(2)
