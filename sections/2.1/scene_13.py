from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
from config import *
from utils import *

class Scene13(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        header = Text("Make-A-Video: Attention Layers", font=DEFAULT_FONT, font_size=40, color=WHITE)
        header.shift(UP * 3.0)
        self.play(FadeIn(header), run_time=0.8)
        self.wait(0.5)

        box_sa = Rectangle(width=3.5, height=1.3, color=BLUE, fill_opacity=0.2)
        box_sa.move_to(LEFT * 2.5 + UP * 0.8)
        lbl_sa = Text("Spatial Attention\n(pretrained T2I weights)", font=DEFAULT_FONT, font_size=20, color=BLUE)
        lbl_sa.move_to(box_sa)
        sa_note = Text("Applied per-frame\nindependently", font=DEFAULT_FONT, font_size=18, color=WHITE)
        sa_note.next_to(box_sa, DOWN, buff=0.2)

        self.play(Create(box_sa), FadeIn(lbl_sa), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(sa_note), run_time=0.5)
        self.wait(0.5)

        box_ta = Rectangle(width=3.5, height=1.3, color=GREEN, fill_opacity=0.2)
        box_ta.move_to(RIGHT * 2.5 + UP * 0.8)
        lbl_ta = Text("Temporal Attention\n(zero initialized)", font=DEFAULT_FONT, font_size=20, color=GREEN)
        lbl_ta.move_to(box_ta)
        ta_note = Text("Learns dynamics\nacross time steps", font=DEFAULT_FONT, font_size=18, color=WHITE)
        ta_note.next_to(box_ta, DOWN, buff=0.2)

        self.play(Create(box_ta), FadeIn(lbl_ta), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(ta_note), run_time=0.5)
        self.wait(0.5)

        zero_meaning = Text(
            "Zero init → identity at start\n(output = spatial attn output only initially)",
            font=DEFAULT_FONT, font_size=22, color=YELLOW
        )
        zero_meaning.shift(DOWN * 2.0)
        self.play(FadeIn(zero_meaning), run_time=1.0)
        self.wait(8.0)

        summary = Text(
            "Both spatial and temporal captured\nwhile preserving T2I prior",
            font=DEFAULT_FONT, font_size=22, color=WHITE
        )
        summary.shift(DOWN * 3.1)
        self.play(FadeIn(summary), run_time=0.8)
        self.wait(5.0)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(2)
