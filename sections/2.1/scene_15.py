from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
from config import *
from utils import *

class Scene15(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        header = Text("WebVid-10M Dataset", font=DEFAULT_FONT, font_size=44, color=WHITE)
        header.shift(UP * 3.0)
        ref = Text("Bain et al., ICCV 2021", font=DEFAULT_FONT, font_size=20, color=WHITE)
        ref.set_opacity(0.6)
        ref.shift(UP * 2.3)
        self.play(FadeIn(header), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(ref), run_time=0.5)
        self.wait(0.5)

        stat_box = Rectangle(width=5.0, height=0.9, color=BLUE, fill_opacity=0.2)
        stat_box.shift(UP * 1.2)
        stat_lbl = Text("10 million video-caption pairs", font=DEFAULT_FONT, font_size=28, color=BLUE)
        stat_lbl.move_to(stat_box)
        self.play(Create(stat_box), FadeIn(stat_lbl), run_time=0.8)
        self.wait(0.5)

        captions = ["Woman by tent\non beach.", "Officer on\nwalkietalkie.", "Billiards\nclose-up."]
        pair_group = VGroup()
        for cap in captions:
            vid_rect = Rectangle(width=2.0, height=1.4, color=GREEN, fill_opacity=0.15)
            cap_txt = Text(cap, font=DEFAULT_FONT, font_size=14, color=WHITE)
            cap_txt.next_to(vid_rect, DOWN, buff=0.15)
            pair_group.add(VGroup(vid_rect, cap_txt))
        pair_group.arrange(RIGHT, buff=0.5)
        pair_group.shift(DOWN * 0.5)
        self.play(FadeIn(pair_group), run_time=1.0)
        self.wait(5.0)

        use_note = Text(
            "Used to teach temporal dynamics\nSpatial quality from image pretraining",
            font=DEFAULT_FONT, font_size=22, color=WHITE
        )
        use_note.shift(DOWN * 2.5)
        self.play(FadeIn(use_note), run_time=0.8)
        self.wait(5.0)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(2)
