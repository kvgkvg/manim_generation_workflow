# SCRIPT.md — Video Generation: Open-Source Base Models Manim Video
**Section:** `2.2`
**Target duration:** ~12 minutes (720s)
**Scene count:** 17 scenes
**Style:** 3Blue1Brown · dark bg · no voiceover
**Manim version:** Community Edition v0.20
**Color palette:** WHITE, BLUE, GREEN, RED, YELLOW, ORANGE (built-ins only)

<!-- Duration budget:
     Title  :   8s  (Scene 1, fixed)
     Body   : 680s  (15 scenes × ~45s each)
     Outro  :  20s  (Scene 17, fixed)
     Total  : ~708s ≈ 11.8 min
-->

---

## NOISE IMPLEMENTATION
NoisySquare uses PIL ImageMobject wrapped in Group (NOT VGroup — ImageMobject is not VMobject).
Key rule: t_ratio=0.0 → clean GREEN, t_ratio=1.0 → pure TV static noise.
Full implementation in shared/utils.py. Always use Group, never VGroup for NoisySquare.

---

## LATEX NOTE
MathTex is unavailable on this system (broken latex.fmt).
Use Text() with unicode characters instead:
  × for \times,  ∘ for \circ,  · for \cdot,  → for \rightarrow
Never use MathTex or Tex.

---

## LAYOUT SAFETY RULES
- All objects: x in [-6.5, 6.5], y in [-3.5, 3.5]
- Labels: always .next_to(ref, DIR, buff=0.3)
- Font: always font=DEFAULT_FONT on every Text()
- No self.add() — every object enters via self.play()
- self.play(FadeOut(*self.mobjects)) at end of every scene
- construct() ends with self.wait(2)
- Layout sketch:
    y= 3.0  top limit
    y= 2.x  header/title
    y= 1.x  sub-labels
    y= 0.x  main visuals
    y=-1.x  secondary
    y=-2.x  captions/notes
    y=-3.0  bottom limit

---

## SCENE 1 — Title Card
**Class:** `Scene1` · **Target:** 8s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `title` | 1.0 | `Text("Video Generation", font=DEFAULT_FONT, font_size=52, color=WHITE)`, UP*0.5 |
| 2 | fade_in | `subtitle` | 0.8 | `Text("2.2 — Open-Source Base Models", font=DEFAULT_FONT, font_size=32, color=BLUE)`, `.next_to(title, DOWN, buff=0.4)` |
| 3 | fade_in | `credit` | 0.5 | `Text("CVPR 2024 Tutorial", font=DEFAULT_FONT, font_size=22, color=WHITE).set_opacity(0.6)`, `.next_to(subtitle, DOWN, buff=0.3)` |
| 4 | wait | — | 3.0 | — |
| 5 | fade_out | all | 1.5 | `FadeOut(VGroup(title,subtitle,credit))` |

**Layout:** y=0.5 title · y=-0.3 subtitle · y=-1.0 credit

---

## SCENE 2 — Open-Source Motivation
**Class:** `Scene2` · **Target:** 45s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("Why Open-Source Models?", font=DEFAULT_FONT, font_size=42, color=WHITE)`, UP*3.0 |
| 2 | create | `closed_box` | 0.8 | `Rectangle(width=3.5, height=0.8, color=RED, fill_opacity=0.2)`, UP*1.5 |
| 3 | fade_in | `closed_lbl` | 0.5 | `Text("Closed-Source: Google · Meta · Nvidia", font=DEFAULT_FONT, font_size=20, color=RED)`, `.move_to(closed_box)` |
| 4 | fade_in | `closed_note` | 0.5 | `Text("Not available to research community", font=DEFAULT_FONT, font_size=20, color=WHITE)`, `.next_to(closed_box, DOWN, buff=0.2)` |
| 5 | fade_in | `arr_down` | 0.5 | `Arrow(UP*0.4, DOWN*0.2, color=WHITE, stroke_width=3)` |
| 6 | create | `open_box` | 0.8 | `Rectangle(width=3.5, height=0.8, color=GREEN, fill_opacity=0.2)`, DOWN*0.5 |
| 7 | fade_in | `open_lbl` | 0.5 | `Text("Open-Source: ModelScope · LaVie · SVD", font=DEFAULT_FONT, font_size=20, color=GREEN)`, `.move_to(open_box)` |
| 8 | fade_in | `open_note` | 0.5 | `Text("Community can use, build, and improve", font=DEFAULT_FONT, font_size=20, color=WHITE)`, `.next_to(open_box, DOWN, buff=0.2)` |
| 9 | wait | — | 10.0 | — |
| 10 | fade_out | all | 1.0 | `FadeOut(*self.mobjects)` |

**Layout:** y=3.0 header · y=1.5 closed_box · y=0.4→-0.2 arrow · y=-0.5 open_box · y=-1.5 notes

---

## SCENE 3 — ModelScopeT2V: Overview
**Class:** `Scene3` · **Target:** 50s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("ModelScopeT2V", font=DEFAULT_FONT, font_size=44, color=WHITE)`, UP*2.8 |
| 2 | fade_in | `ref` | 0.5 | `Text("Wang et al., arXiv 2023", font=DEFAULT_FONT, font_size=18, color=WHITE).set_opacity(0.6)`, UP*2.1 |
| 3 | fade_in | `key_idea` | 0.6 | `Text("Leverage pretrained Stable Diffusion for video", font=DEFAULT_FONT, font_size=26, color=YELLOW)`, UP*1.4 |
| 4 | create | `sd_box` | 0.7 | `Rectangle(width=3.0, height=0.8, color=BLUE, fill_opacity=0.2)`, LEFT*2.5+UP*0.2 |
| 5 | fade_in | `sd_lbl` | 0.5 | `Text("Stable Diffusion\n(pretrained T2I)", font=DEFAULT_FONT, font_size=20, color=BLUE)`, `.move_to(sd_box)` |
| 6 | fade_in | `arr_inflate` | 0.5 | `Arrow(sd_box.get_right(), RIGHT*0.6+UP*0.2, color=WHITE, stroke_width=3, buff=0.05)` |
| 7 | fade_in | `inflate_lbl` | 0.4 | `Text("inflate\nto 3D", font=DEFAULT_FONT, font_size=18, color=WHITE)`, `.next_to(arr_inflate, UP, buff=0.1)` |
| 8 | create | `ms_box` | 0.7 | `Rectangle(width=3.2, height=0.8, color=GREEN, fill_opacity=0.2)`, RIGHT*2.8+UP*0.2 |
| 9 | fade_in | `ms_lbl` | 0.5 | `Text("ModelScopeT2V\n(3D video model)", font=DEFAULT_FONT, font_size=20, color=GREEN)`, `.move_to(ms_box)` |
| 10 | wait | — | 8.0 | — |
| 11 | fade_in | `bullets` | 0.8 | Three `Text` lines: "• Preserve all SD pretrained weights" / "• Insert spatio-temporal blocks" / "• Handle varying number of frames", stacked at DOWN*1.2/1.8/2.4 left-aligned at x=-4.0, font_size=22, color=WHITE |
| 12 | wait | — | 8.0 | — |
| 13 | fade_out | all | 1.0 | `FadeOut(*self.mobjects)` |

**Layout:** y=2.8 header · y=2.1 ref · y=1.4 key_idea · y=0.2 SD→MS pipeline · y=-1.2/-1.8/-2.4 bullets

---

## SCENE 4 — ModelScopeT2V: Architecture
**Class:** `Scene4` · **Target:** 50s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("ModelScopeT2V Architecture", font=DEFAULT_FONT, font_size=38, color=WHITE)`, UP*3.0 |
| 2 | create | `latent_box` | 0.7 | `Rectangle(width=2.8, height=0.8, color=BLUE, fill_opacity=0.2)`, LEFT*3.5+UP*1.0 |
| 3 | fade_in | `latent_lbl` | 0.5 | `Text("Latent\nDiffusion (SD)", font=DEFAULT_FONT, font_size=19, color=BLUE)`, `.move_to(latent_box)` |
| 4 | create | `spatial_box` | 0.7 | `Rectangle(width=2.8, height=0.8, color=YELLOW, fill_opacity=0.2)`, LEFT*0.2+UP*1.0 |
| 5 | fade_in | `spatial_lbl` | 0.5 | `Text("Spatial 2D Conv\n(SD weights)", font=DEFAULT_FONT, font_size=19, color=YELLOW)`, `.move_to(spatial_box)` |
| 6 | create | `temp_conv_box` | 0.7 | `Rectangle(width=2.8, height=0.8, color=ORANGE, fill_opacity=0.2)`, RIGHT*3.3+UP*1.0 |
| 7 | fade_in | `temp_conv_lbl` | 0.5 | `Text("Temporal Conv\n(1D, new)", font=DEFAULT_FONT, font_size=19, color=ORANGE)`, `.move_to(temp_conv_box)` |
| 8 | create | `temp_attn_box` | 0.7 | `Rectangle(width=2.8, height=0.8, color=GREEN, fill_opacity=0.2)`, RIGHT*3.3+DOWN*0.2 |
| 9 | fade_in | `temp_attn_lbl` | 0.5 | `Text("Temporal Attn\n(new)", font=DEFAULT_FONT, font_size=19, color=GREEN)`, `.move_to(temp_attn_box)` |
| 10 | fade_in | `arrows` | 0.8 | `Arrow` from latent→spatial, spatial→temp_conv, spatial→temp_attn, `stroke_width=2, color=WHITE` |
| 11 | wait | — | 8.0 | — |
| 12 | fade_in | `note` | 0.8 | `Text("Same (2+1)D factorization as before:\nspatial SD weights + new temporal layers", font=DEFAULT_FONT, font_size=22, color=WHITE)`, DOWN*2.3 |
| 13 | wait | — | 5.0 | — |
| 14 | fade_out | all | 1.0 | `FadeOut(*self.mobjects)` |

**Layout:** y=3.0 header · y=1.0 latent/spatial/temp boxes · y=-0.2 temp_attn · y=-2.3 note

---

## SCENE 5 — ModelScopeT2V: Variable-Length Sequences
**Class:** `Scene5` · **Target:** 45s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("Variable-Length Sequence Handling", font=DEFAULT_FONT, font_size=38, color=WHITE)`, UP*3.0 |
| 2 | fade_in | `idea` | 0.6 | `Text("Both temporal conv and attention support any T", font=DEFAULT_FONT, font_size=24, color=YELLOW)`, UP*2.1 |
| 3 | fade_in | `t_short_lbl` | 0.5 | `Text("Short video (T=4):", font=DEFAULT_FONT, font_size=22, color=WHITE)`, LEFT*3.5+UP*0.8 |
| 4 | create | `frames_short` | 0.8 | `VGroup` of 4 `Square(side_length=0.7, color=BLUE, fill_opacity=0.2)` arranged RIGHT buff=0.2, `.next_to(t_short_lbl, RIGHT, buff=0.3)` |
| 5 | fade_in | `t_long_lbl` | 0.5 | `Text("Long video (T=16):", font=DEFAULT_FONT, font_size=22, color=WHITE)`, LEFT*3.5+DOWN*0.3 |
| 6 | create | `frames_long` | 0.8 | `VGroup` of 8 `Square(side_length=0.6, color=GREEN, fill_opacity=0.2)` arranged RIGHT buff=0.15, `.next_to(t_long_lbl, RIGHT, buff=0.3)` + `Text("···")` |
| 7 | wait | — | 5.0 | — |
| 8 | fade_in | `benefit` | 0.8 | `Text("Benefit: train on both images AND videos\nby setting T=1 or T>1", font=DEFAULT_FONT, font_size=24, color=WHITE)`, DOWN*1.8 |
| 9 | wait | — | 8.0 | — |
| 10 | fade_out | all | 1.0 | `FadeOut(*self.mobjects)` |

**Layout:** y=3.0 header · y=2.1 idea · y=0.8 short · y=-0.3 long · y=-1.8 benefit

---

## SCENE 6 — ModelScopeT2V: Dual Image-Video Training
**Class:** `Scene6` · **Target:** 45s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("T=1: Dual Image-Video Training", font=DEFAULT_FONT, font_size=40, color=WHITE)`, UP*3.0 |
| 2 | fade_in | `idea` | 0.6 | `Text("When T=1, temporal layers have no effect", font=DEFAULT_FONT, font_size=26, color=YELLOW)`, UP*2.1 |
| 3 | create | `video_box` | 0.7 | `Rectangle(width=3.2, height=0.8, color=GREEN, fill_opacity=0.2)`, LEFT*2.5+UP*0.5 |
| 4 | fade_in | `video_lbl` | 0.5 | `Text("Video input (T>1)\n→ video generation", font=DEFAULT_FONT, font_size=19, color=GREEN)`, `.move_to(video_box)` |
| 5 | create | `image_box` | 0.7 | `Rectangle(width=3.2, height=0.8, color=BLUE, fill_opacity=0.2)`, RIGHT*2.5+UP*0.5 |
| 6 | fade_in | `image_lbl` | 0.5 | `Text("Image input (T=1)\n→ image generation", font=DEFAULT_FONT, font_size=19, color=BLUE)`, `.move_to(image_box)` |
| 7 | fade_in | `same_model` | 0.8 | `Text("Same model — same weights!", font=DEFAULT_FONT, font_size=26, color=ORANGE)`, DOWN*0.5 |
| 8 | wait | — | 8.0 | — |
| 9 | fade_in | `benefit` | 0.8 | `Text("Train on large image datasets + smaller video datasets\n→ better generalization", font=DEFAULT_FONT, font_size=22, color=WHITE)`, DOWN*1.8 |
| 10 | wait | — | 5.0 | — |
| 11 | fade_out | all | 1.0 | `FadeOut(*self.mobjects)` |

**Layout:** y=3.0 header · y=2.1 idea · y=0.5 two boxes · y=-0.5 same_model · y=-1.8 benefit

---

## SCENE 7 — ZeroScope: HQ Finetuning
**Class:** `Scene7` · **Target:** 40s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("ZeroScope", font=DEFAULT_FONT, font_size=48, color=WHITE)`, UP*2.5 |
| 2 | fade_in | `sub` | 0.5 | `Text("Open-source finetune of ModelScope", font=DEFAULT_FONT, font_size=24, color=WHITE).set_opacity(0.7)`, UP*1.7 |
| 3 | fade_in | `problem` | 0.8 | `Text("Problem: ModelScope generates Shutterstock watermarks", font=DEFAULT_FONT, font_size=22, color=RED)`, UP*0.6 |
| 4 | fade_in | `arr_solve` | 0.5 | `Arrow(UP*0.0, DOWN*0.6, color=WHITE, stroke_width=3)` |
| 5 | create | `fix_box` | 0.7 | `Rectangle(width=5.5, height=0.8, color=GREEN, fill_opacity=0.2)`, DOWN*1.0 |
| 6 | fade_in | `fix_lbl` | 0.5 | `Text("Finetune on smaller high-quality watermark-free dataset", font=DEFAULT_FONT, font_size=20, color=GREEN)`, `.move_to(fix_box)` |
| 7 | wait | — | 5.0 | — |
| 8 | fade_in | `result` | 0.8 | `Text("Result: 1024×576 resolution · no watermarks · cleaner output", font=DEFAULT_FONT, font_size=22, color=YELLOW)`, DOWN*2.2 |
| 9 | wait | — | 5.0 | — |
| 10 | fade_out | all | 1.0 | `FadeOut(*self.mobjects)` |

**Layout:** y=2.5 title · y=1.7 sub · y=0.6 problem · y=0→-0.6 arrow · y=-1.0 fix_box · y=-2.2 result

---

## SCENE 8 — Show-1: Text Alignment Problem
**Class:** `Scene8` · **Target:** 45s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("Show-1", font=DEFAULT_FONT, font_size=48, color=WHITE)`, UP*2.8 |
| 2 | fade_in | `ref` | 0.5 | `Text("Zhang et al., arXiv 2023", font=DEFAULT_FONT, font_size=18, color=WHITE).set_opacity(0.6)`, UP*2.1 |
| 3 | fade_in | `problem_lbl` | 0.6 | `Text("Problem: latent VDMs struggle with text alignment", font=DEFAULT_FONT, font_size=26, color=YELLOW)`, UP*1.4 |
| 4 | create | `example_box` | 0.8 | `Rectangle(width=9.0, height=1.0, color=GRAY, fill_opacity=0.1)`, UP*0.3 |
| 5 | fade_in | `prompt_lbl` | 0.5 | `Text('Prompt: "panda by waterfall holding sign saying \'Show Lab\'"', font=DEFAULT_FONT, font_size=18, color=WHITE)`, `.move_to(example_box)` |
| 6 | fade_in | `ms_fail` | 0.7 | `Text("ModelScope: panda OK, waterfall OK — NO SIGN", font=DEFAULT_FONT, font_size=20, color=RED)`, DOWN*0.7 |
| 7 | fade_in | `gen2_fail` | 0.7 | `Text("Gen-2: also fails to render the sign", font=DEFAULT_FONT, font_size=20, color=RED)`, DOWN*1.3 |
| 8 | wait | — | 8.0 | — |
| 9 | fade_in | `question` | 0.8 | `Text("Why do latent models fail? → Compressed latent loses fine text detail", font=DEFAULT_FONT, font_size=22, color=WHITE)`, DOWN*2.3 |
| 10 | wait | — | 5.0 | — |
| 11 | fade_out | all | 1.0 | `FadeOut(*self.mobjects)` |

**Layout:** y=2.8 header · y=2.1 ref · y=1.4 problem · y=0.3 example_box · y=-0.7/-1.3 fails · y=-2.3 question

---

## SCENE 9 — Show-1: Pixel vs Latent Trade-off
**Class:** `Scene9` · **Target:** 50s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("Pixel Space vs Latent Space", font=DEFAULT_FONT, font_size=40, color=WHITE)`, UP*3.0 |
| 2 | create | `box_pixel` | 0.7 | `Rectangle(width=3.5, height=1.6, color=BLUE, fill_opacity=0.15)`, LEFT*2.8+UP*0.5 |
| 3 | fade_in | `pixel_title` | 0.5 | `Text("Pixel-based VDM", font=DEFAULT_FONT, font_size=22, color=BLUE)`, `.next_to(box_pixel, UP, buff=0.15)` |
| 4 | fade_in | `pixel_pros` | 0.5 | `Text("✓ Better text alignment\n✓ Fine detail preserved", font=DEFAULT_FONT, font_size=19, color=GREEN)`, `.move_to(box_pixel.get_center()+UP*0.25)` |
| 5 | fade_in | `pixel_cons` | 0.5 | `Text("✗ High memory (full pixel res)", font=DEFAULT_FONT, font_size=19, color=RED)`, `.move_to(box_pixel.get_center()+DOWN*0.4)` |
| 6 | create | `box_latent` | 0.7 | `Rectangle(width=3.5, height=1.6, color=ORANGE, fill_opacity=0.15)`, RIGHT*2.8+UP*0.5 |
| 7 | fade_in | `latent_title` | 0.5 | `Text("Latent-based VDM", font=DEFAULT_FONT, font_size=22, color=ORANGE)`, `.next_to(box_latent, UP, buff=0.15)` |
| 8 | fade_in | `latent_pros` | 0.5 | `Text("✓ Low memory\n✓ Fast training", font=DEFAULT_FONT, font_size=19, color=GREEN)`, `.move_to(box_latent.get_center()+UP*0.25)` |
| 9 | fade_in | `latent_cons` | 0.5 | `Text("✗ Weaker text alignment\n  at low resolution", font=DEFAULT_FONT, font_size=19, color=RED)`, `.move_to(box_latent.get_center()+DOWN*0.4)` |
| 10 | wait | — | 8.0 | — |
| 11 | fade_in | `solution` | 0.8 | `Text("Show-1 idea: use BOTH — pixel at low-res, latent at high-res", font=DEFAULT_FONT, font_size=22, color=YELLOW)`, DOWN*2.5 |
| 12 | wait | — | 5.0 | — |
| 13 | fade_out | all | 1.0 | `FadeOut(*self.mobjects)` |

**Layout:** y=3.0 header · y=0.5 two boxes · y=1.6 box titles · y=-2.5 solution

---

## SCENE 10 — Show-1: Hybrid Pipeline
**Class:** `Scene10` · **Target:** 50s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("Show-1: Hybrid Pipeline", font=DEFAULT_FONT, font_size=40, color=WHITE)`, UP*3.0 |
| 2 | fade_in | `input_lbl` | 0.5 | `Text("Text\nPrompt", font=DEFAULT_FONT, font_size=18, color=WHITE)`, LEFT*5.5+UP*0.0 |
| 3 | create | `box_kf` | 0.7 | `Rectangle(width=2.0, height=0.8, color=BLUE, fill_opacity=0.25)`, LEFT*2.8+UP*0.0 |
| 4 | fade_in | `lbl_kf` | 0.4 | `Text("Pixel VDM\nKeyframes", font=DEFAULT_FONT, font_size=16, color=BLUE)`, `.move_to(box_kf)` |
| 5 | create | `box_interp` | 0.7 | `Rectangle(width=2.0, height=0.8, color=BLUE, fill_opacity=0.25)`, LEFT*0.1+UP*0.0 |
| 6 | fade_in | `lbl_interp` | 0.4 | `Text("Pixel VDM\nInterpolation", font=DEFAULT_FONT, font_size=16, color=BLUE)`, `.move_to(box_interp)` |
| 7 | create | `box_sr` | 0.7 | `Rectangle(width=2.0, height=0.8, color=ORANGE, fill_opacity=0.25)`, RIGHT*2.6+UP*0.0 |
| 8 | fade_in | `lbl_sr` | 0.4 | `Text("Latent VDM\nSuper-Res", font=DEFAULT_FONT, font_size=16, color=ORANGE)`, `.move_to(box_sr)` |
| 9 | fade_in | `arrows_pipe` | 0.8 | Arrows connecting input→kf→interp→sr, `stroke_width=2, color=WHITE` |
| 10 | fade_in | `out_res` | 0.5 | `Text("Final HQ\nvideo", font=DEFAULT_FONT, font_size=18, color=WHITE)`, RIGHT*5.0+UP*0.0 |
| 11 | wait | — | 8.0 | — |
| 12 | fade_in | `key` | 0.8 | `Text("Pixel at low-res (manageable memory)\nLatent at final SR (too large for pixel)", font=DEFAULT_FONT, font_size=22, color=WHITE)`, DOWN*2.0 |
| 13 | wait | — | 8.0 | — |
| 14 | fade_out | all | 1.0 | `FadeOut(*self.mobjects)` |

**Layout:** y=3.0 header · y=0.0 pipeline boxes · y=-2.0 key note

---

## SCENE 11 — VideoCrafter Overview
**Class:** `Scene11` · **Target:** 40s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("VideoCrafter", font=DEFAULT_FONT, font_size=48, color=WHITE)`, UP*2.5 |
| 2 | fade_in | `ref` | 0.5 | `Text("Chen et al., arXiv 2023", font=DEFAULT_FONT, font_size=20, color=WHITE).set_opacity(0.6)`, UP*1.7 |
| 3 | fade_in | `approach` | 0.6 | `Text("Approach: latent diffusion + temporal layers", font=DEFAULT_FONT, font_size=26, color=YELLOW)`, UP*0.8 |
| 4 | create | `arch_box` | 0.8 | `Rectangle(width=6.0, height=1.2, color=BLUE, fill_opacity=0.15)`, DOWN*0.3 |
| 5 | fade_in | `arch_lbl` | 0.5 | `Text("SD (latent space)  +  Temporal Conv  +  Temporal Attn", font=DEFAULT_FONT, font_size=20, color=BLUE)`, `.move_to(arch_box)` |
| 6 | wait | — | 5.0 | — |
| 7 | fade_in | `note` | 0.8 | `Text("Similar architecture to Align your Latents\nHigh-quality open-source video generation", font=DEFAULT_FONT, font_size=22, color=WHITE)`, DOWN*1.9 |
| 8 | wait | — | 5.0 | — |
| 9 | fade_out | all | 1.0 | `FadeOut(*self.mobjects)` |

**Layout:** y=2.5 header · y=1.7 ref · y=0.8 approach · y=-0.3 arch_box · y=-1.9 note

---

## SCENE 12 — LaVie: Dataset + Joint Training
**Class:** `Scene12` · **Target:** 45s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("LaVie", font=DEFAULT_FONT, font_size=48, color=WHITE)`, UP*2.8 |
| 2 | fade_in | `ref` | 0.5 | `Text("Wang et al., NTU — arXiv 2023", font=DEFAULT_FONT, font_size=20, color=WHITE).set_opacity(0.6)`, UP*2.1 |
| 3 | fade_in | `key` | 0.6 | `Text("Joint image-video finetuning + new dataset", font=DEFAULT_FONT, font_size=26, color=YELLOW)`, UP*1.4 |
| 4 | create | `data_box` | 0.8 | `Rectangle(width=4.5, height=0.8, color=BLUE, fill_opacity=0.2)`, UP*0.3 |
| 5 | fade_in | `data_lbl` | 0.5 | `Text("Vimeo25M: 25 million high-quality video-text pairs", font=DEFAULT_FONT, font_size=20, color=BLUE)`, `.move_to(data_box)` |
| 6 | fade_in | `compare` | 0.7 | `Text("vs WebVid-10M (10M clips, lower quality)", font=DEFAULT_FONT, font_size=20, color=WHITE).set_opacity(0.7)`, DOWN*0.6 |
| 7 | fade_in | `result` | 0.8 | `Text("Higher quality data → better resolution & motion quality", font=DEFAULT_FONT, font_size=22, color=GREEN)`, DOWN*1.5 |
| 8 | wait | — | 8.0 | — |
| 9 | fade_in | `arch_note` | 0.7 | `Text("Architecture: cascaded latent diffusion (similar to LDM + temporal)", font=DEFAULT_FONT, font_size=20, color=WHITE)`, DOWN*2.5 |
| 10 | wait | — | 5.0 | — |
| 11 | fade_out | all | 1.0 | `FadeOut(*self.mobjects)` |

**Layout:** y=2.8 header · y=2.1 ref · y=1.4 key · y=0.3 data_box · y=-0.6 compare · y=-1.5 result · y=-2.5 arch_note

---

## SCENE 13 — SVD: Data Curation Pipeline
**Class:** `Scene13` · **Target:** 50s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("Stable Video Diffusion (SVD)", font=DEFAULT_FONT, font_size=38, color=WHITE)`, UP*3.0 |
| 2 | fade_in | `ref` | 0.5 | `Text("Blattmann et al., Stability AI 2023", font=DEFAULT_FONT, font_size=18, color=WHITE).set_opacity(0.6)`, UP*2.3 |
| 3 | fade_in | `focus` | 0.6 | `Text("Key contribution: systematic data curation", font=DEFAULT_FONT, font_size=26, color=YELLOW)`, UP*1.6 |
| 4 | create | `step1` | 0.6 | `Rectangle(width=2.4, height=0.7, color=BLUE, fill_opacity=0.2)`, LEFT*4.0+UP*0.5 |
| 5 | fade_in | `s1_lbl` | 0.4 | `Text("Cut Detection\n& Clipping", font=DEFAULT_FONT, font_size=16, color=BLUE)`, `.move_to(step1)` |
| 6 | fade_in | `arr12` | 0.3 | `Arrow(step1.get_right(), LEFT*1.5+UP*0.5, color=WHITE, stroke_width=2, buff=0.05)` |
| 7 | create | `step2` | 0.6 | `Rectangle(width=2.4, height=0.7, color=GREEN, fill_opacity=0.2)`, LEFT*0.0+UP*0.5 |
| 8 | fade_in | `s2_lbl` | 0.4 | `Text("Synthetic\nCaptioning", font=DEFAULT_FONT, font_size=16, color=GREEN)`, `.move_to(step2)` |
| 9 | fade_in | `arr23` | 0.3 | `Arrow(step2.get_right(), RIGHT*2.5+UP*0.5, color=WHITE, stroke_width=2, buff=0.05)` |
| 10 | create | `step3` | 0.6 | `Rectangle(width=2.4, height=0.7, color=ORANGE, fill_opacity=0.2)`, RIGHT*4.0+UP*0.5 |
| 11 | fade_in | `s3_lbl` | 0.4 | `Text("CLIP + Aesthetic\nScoring", font=DEFAULT_FONT, font_size=16, color=ORANGE)`, `.move_to(step3)` |
| 12 | fade_in | `filter_steps` | 0.8 | Two `Text` lines: "• Static scene filtering (optical flow)" / "• Text/OCR detection filter", at DOWN*1.4 and DOWN*2.0, font_size=22, color=WHITE |
| 13 | wait | — | 8.0 | — |
| 14 | fade_out | all | 1.0 | `FadeOut(*self.mobjects)` |

**Layout:** y=3.0 header · y=2.3 ref · y=1.6 focus · y=0.5 pipeline steps · y=-1.4/-2.0 filter notes

---

## SCENE 14 — SVD: LVD Dataset Stats
**Class:** `Scene14` · **Target:** 40s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("SVD: Large Video Dataset (LVD)", font=DEFAULT_FONT, font_size=40, color=WHITE)`, UP*3.0 |
| 2 | create | `row1` | 0.7 | `Rectangle(width=7.0, height=0.7, color=BLUE, fill_opacity=0.2)`, UP*1.5 |
| 3 | fade_in | `lbl1` | 0.5 | `Text("LVD: 580M video clips · >200 years total duration", font=DEFAULT_FONT, font_size=20, color=BLUE)`, `.move_to(row1)` |
| 4 | create | `row2` | 0.7 | `Rectangle(width=7.0, height=0.7, color=GREEN, fill_opacity=0.2)`, UP*0.5 |
| 5 | fade_in | `lbl2` | 0.5 | `Text("LVD-10M: 10M clips subset (~3 years)", font=DEFAULT_FONT, font_size=20, color=GREEN)`, `.move_to(row2)` |
| 6 | create | `row3` | 0.7 | `Rectangle(width=7.0, height=0.7, color=YELLOW, fill_opacity=0.2)`, DOWN*0.5 |
| 7 | fade_in | `lbl3` | 0.5 | `Text("After filtering: ~2M clips (25% retained)", font=DEFAULT_FONT, font_size=20, color=YELLOW)`, `.move_to(row3)` |
| 8 | wait | — | 5.0 | — |
| 9 | fade_in | `key` | 0.8 | `Text("Quality beats quantity: well-curated > un-curated", font=DEFAULT_FONT, font_size=24, color=ORANGE)`, DOWN*1.7 |
| 10 | wait | — | 5.0 | — |
| 11 | fade_out | all | 1.0 | `FadeOut(*self.mobjects)` |

**Layout:** y=3.0 header · y=1.5/0.5/-0.5 dataset rows · y=-1.7 key

---

## SCENE 15 — SVD: Stages 1 & 2
**Class:** `Scene15` · **Target:** 45s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("SVD: Training Stages 1 & 2", font=DEFAULT_FONT, font_size=40, color=WHITE)`, UP*3.0 |
| 2 | create | `box1` | 0.7 | `Rectangle(width=5.5, height=0.8, color=BLUE, fill_opacity=0.2)`, UP*1.5 |
| 3 | fade_in | `lbl1` | 0.5 | `Text("Stage 1: Init from SD 2.1 → inflate 2D to 3D", font=DEFAULT_FONT, font_size=20, color=BLUE)`, `.move_to(box1)` |
| 4 | fade_in | `arr12` | 0.4 | `Arrow(box1.get_bottom(), UP*0.4, color=WHITE, stroke_width=2, buff=0.05)` |
| 5 | create | `box2` | 0.7 | `Rectangle(width=5.5, height=0.8, color=GREEN, fill_opacity=0.2)`, UP*0.0 |
| 6 | fade_in | `lbl2` | 0.5 | `Text("Stage 2: Pretrain on LVD (large-scale video)", font=DEFAULT_FONT, font_size=20, color=GREEN)`, `.move_to(box2)` |
| 7 | wait | — | 5.0 | — |
| 8 | fade_in | `note` | 0.8 | `Text("Same pattern as ModelScope → ZeroScope:\nstart broad, then curate and finetune", font=DEFAULT_FONT, font_size=22, color=WHITE)`, DOWN*1.5 |
| 9 | wait | — | 8.0 | — |
| 10 | fade_out | all | 1.0 | `FadeOut(*self.mobjects)` |

**Layout:** y=3.0 header · y=1.5 box1 · y=1.0→0.4 arrow · y=0.0 box2 · y=-1.5 note

---

## SCENE 16 — SVD: High-Quality Finetuning (Stage 3)
**Class:** `Scene16` · **Target:** 40s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("SVD: Stage 3 — High-Quality Finetuning", font=DEFAULT_FONT, font_size=36, color=WHITE)`, UP*3.0 |
| 2 | create | `box_hq` | 0.8 | `Rectangle(width=5.5, height=0.8, color=ORANGE, fill_opacity=0.2)`, UP*1.5 |
| 3 | fade_in | `hq_lbl` | 0.5 | `Text("Finetune on ~1M high-quality clips at 576×1024", font=DEFAULT_FONT, font_size=20, color=ORANGE)`, `.move_to(box_hq)` |
| 4 | fade_in | `capabilities` | 1.0 | Four `Text` lines stacked: "• Text-to-video generation" / "• Image-to-video generation" / "• Frame interpolation" / "• Multi-view generation", DOWN*0.2 to DOWN*2.0, font_size=22, color=WHITE |
| 5 | wait | — | 8.0 | — |
| 6 | fade_in | `key` | 0.8 | `Text("Curation gains persist after finetuning", font=DEFAULT_FONT, font_size=22, color=YELLOW)`, DOWN*2.5 |
| 7 | wait | — | 3.0 | — |
| 8 | fade_out | all | 1.0 | `FadeOut(*self.mobjects)` |

**Layout:** y=3.0 header · y=1.5 hq_box · y=-0.2 to -2.0 capabilities · y=-2.5 key

---

## SCENE 17 — Summary & Outro
**Class:** `Scene17` · **Target:** 20s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `title` | 0.8 | `Text("Section 2.2 — Key Takeaways", font=DEFAULT_FONT, font_size=38, color=WHITE)`, UP*2.8 |
| 2 | fade_in | `t1` | 0.5 | `Text("1. Open-source = community access to strong video models", font=DEFAULT_FONT, font_size=22, color=BLUE)`, UP*1.6 |
| 3 | fade_in | `t2` | 0.5 | `Text("2. ModelScope: inflate SD + (2+1)D conv, T=1 dual training", font=DEFAULT_FONT, font_size=22, color=GREEN)`, UP*0.8 |
| 4 | fade_in | `t3` | 0.5 | `Text("3. Show-1: pixel (alignment) + latent (efficiency) hybrid", font=DEFAULT_FONT, font_size=22, color=YELLOW)`, UP*0.0 |
| 5 | fade_in | `t4` | 0.5 | `Text("4. LaVie: quality data (Vimeo25M) beats quantity", font=DEFAULT_FONT, font_size=22, color=ORANGE)`, DOWN*0.8 |
| 6 | fade_in | `t5` | 0.5 | `Text("5. SVD: systematic curation + 3-stage training", font=DEFAULT_FONT, font_size=22, color=WHITE)`, DOWN*1.6 |
| 7 | wait | — | 5.0 | — |
| 8 | fade_out | all | 2.0 | `FadeOut(*self.mobjects)` |

**Layout:** y=2.8 title · y=1.6/0.8/0.0/-0.8/-1.6 takeaways
