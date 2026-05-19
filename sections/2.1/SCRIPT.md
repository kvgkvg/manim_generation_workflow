# SCRIPT.md — Video Generation: Pioneering Works Manim Video
**Section:** `2.1`
**Target duration:** ~15 minutes (900s)
**Scene count:** 21 scenes
**Style:** 3Blue1Brown · dark bg · no voiceover
**Manim version:** Community Edition v0.19
**Color palette:** WHITE, BLUE, GREEN, RED, YELLOW, ORANGE (built-ins only)

<!-- Duration budget:
     Title  :   8s  (Scene 1, fixed)
     Body   : 884s  (19 scenes × ~46s each)
     Outro  :  20s  (Scene 21, fixed)
     Total  : ~912s ≈ 15.2 min
-->

---

## NOISE IMPLEMENTATION
NoisySquare uses PIL ImageMobject, NOT fill_color=WHITE.

Key rule: t_ratio=0.0 → clean GREEN, t_ratio=1.0 → pure TV static noise.
Green channel must reach 0 at t_ratio=1.0 — no color tint on pure noise.
Full implementation is in shared/utils.py.

---

## LAYOUT SAFETY RULES
- All objects: x in [-6.5, 6.5], y in [-3.5, 3.5]
- Labels: always .next_to(ref, DIR, buff=0.3) — no hardcoded y near other elements
- Two text objects at same y: must have horizontal separation ≥ 2.0
- Font sizes: title=44, body=30–34, label=22–26, tiny=18–20
- VGroup too wide: .scale_to_fit_width(11.5)
- Verify layout sketch before writing each scene:
    y= 3.0  top limit
    y= 2.x  labels/titles
    y= 1.x  equations
    y= 0.x  main visuals
    y=-1.x  secondary
    y=-2.x  captions
    y=-3.0  bottom limit

---

## SCENE 1 — Title Card
**Class:** `Scene1` · **Target:** 8s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `title` | 1.0 | `Text("Video Generation", font_size=52, color=WHITE)`, position=ORIGIN+UP*0.5 |
| 2 | fade_in | `subtitle` | 0.8 | `Text("2.1 — Pioneering & Early Works", font_size=32, color=BLUE)`, `.next_to(title, DOWN, buff=0.4)` |
| 3 | fade_in | `credit` | 0.5 | `Text("CVPR 2024 Tutorial", font_size=22, color=WHITE).set_opacity(0.6)`, `.next_to(subtitle, DOWN, buff=0.3)` |
| 4 | wait | — | 3.0 | — |
| 5 | fade_out | `VGroup(title, subtitle, credit)` | 1.5 | — |

**Layout:**
```
y= 0.5  title
y=-0.3  subtitle
y=-1.0  credit
```

---

## SCENE 2 — Field Overview: Taxonomy
**Class:** `Scene2` · **Target:** 45s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("Video Generation Landscape", font_size=40, color=WHITE)`, position=UP*3.0 |
| 2 | create | `center_box` | 0.8 | `Rectangle(width=2.8, height=0.7, color=BLUE).shift(UP*1.2)` |
| 3 | fade_in | `center_lbl` | 0.5 | `Text("Video Generation", font_size=24, color=BLUE)`, `.move_to(center_box)` |
| 4 | create | `arr_left` | 0.5 | `Arrow(center_box.get_left(), LEFT*4.5+UP*1.2, color=WHITE, stroke_width=2)` |
| 5 | create | `arr_right` | 0.5 | `Arrow(center_box.get_right(), RIGHT*4.5+UP*1.2, color=WHITE, stroke_width=2)` |
| 6 | create | `arr_down` | 0.5 | `Arrow(center_box.get_bottom(), DOWN*0.3+UP*0.2, color=WHITE, stroke_width=2)` |
| 7 | fade_in | `box_pixel` | 0.6 | `Rectangle(width=2.4, height=0.6, color=GREEN).move_to(LEFT*4.5+UP*1.2)` |
| 8 | fade_in | `lbl_pixel` | 0.4 | `Text("Pixel Space", font_size=22, color=GREEN)`, `.move_to(box_pixel)` |
| 9 | fade_in | `box_latent` | 0.6 | `Rectangle(width=2.4, height=0.6, color=YELLOW).move_to(RIGHT*4.5+UP*1.2)` |
| 10 | fade_in | `lbl_latent` | 0.4 | `Text("Latent Space", font_size=22, color=YELLOW)`, `.move_to(box_latent)` |
| 11 | fade_in | `box_cascade` | 0.6 | `Rectangle(width=2.4, height=0.6, color=ORANGE).move_to(UP*0.2)` |
| 12 | fade_in | `lbl_cascade` | 0.4 | `Text("Cascaded", font_size=22, color=ORANGE)`, `.move_to(box_cascade)` |
| 13 | fade_in | `works_pixel` | 0.8 | `Text("VDM · Make-A-Video\nImagen Video", font_size=18, color=WHITE)`, `.next_to(box_pixel, DOWN, buff=0.25)` |
| 14 | fade_in | `works_latent` | 0.8 | `Text("Align your Latents\nVideoCrafter", font_size=18, color=WHITE)`, `.next_to(box_latent, DOWN, buff=0.25)` |
| 15 | wait | — | 5.0 | — |
| 16 | fade_in | `note` | 0.6 | `Text("Focus: pioneering works from 2022–2023", font_size=22, color=BLUE)`, position=DOWN*2.8 |
| 17 | wait | — | 5.0 | — |
| 18 | fade_out | `VGroup(header,center_box,center_lbl,arr_left,arr_right,arr_down,box_pixel,lbl_pixel,box_latent,lbl_latent,box_cascade,lbl_cascade,works_pixel,works_latent,note)` | 1.0 | — |

**Layout:**
```
y= 3.0  header
y= 1.2  center_box (Video Generation)
y= 1.2  arr_left → box_pixel at (-4.5, 1.2)
y= 1.2  arr_right → box_latent at (4.5, 1.2)
y= 0.2  box_cascade
y=-0.7  works_pixel / works_latent
y=-2.8  note
```

---

## SCENE 3 — T2I vs T2V Problem Definition
**Class:** `Scene3` · **Target:** 50s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("Problem Definition", font_size=44, color=WHITE)`, position=UP*3.0 |
| 2 | create | `divider` | 0.5 | `Line(UP*2.5, DOWN*2.5, color=WHITE, stroke_width=1).set_opacity(0.4)` |
| 3 | fade_in | `lbl_t2i` | 0.6 | `Text("Text-to-Image (T2I)", font_size=28, color=BLUE)`, position=LEFT*3.2+UP*2.0 |
| 4 | fade_in | `lbl_t2v` | 0.6 | `Text("Text-to-Video (T2V)", font_size=28, color=GREEN)`, position=RIGHT*3.2+UP*2.0 |
| 5 | create | `text_box_i` | 0.8 | `Rectangle(width=4.5, height=0.7, color=BLUE).move_to(LEFT*3.2+UP*1.0)` |
| 6 | fade_in | `text_lbl_i` | 0.5 | `Text('"Toad practicing karate."', font_size=18, color=WHITE)`, `.move_to(text_box_i)` |
| 7 | create | `text_box_v` | 0.8 | `Rectangle(width=4.5, height=0.7, color=GREEN).move_to(RIGHT*3.2+UP*1.0)` |
| 8 | fade_in | `text_lbl_v` | 0.5 | `Text('"Toad practicing karate."', font_size=18, color=WHITE)`, `.move_to(text_box_v)` |
| 9 | fade_in | `arr_i` | 0.5 | `Arrow(LEFT*3.2+UP*0.4, LEFT*3.2+DOWN*0.2, color=WHITE, stroke_width=3)` |
| 10 | fade_in | `arr_v` | 0.5 | `Arrow(RIGHT*3.2+UP*0.4, RIGHT*3.2+DOWN*0.2, color=WHITE, stroke_width=3)` |
| 11 | create | `img_box` | 0.8 | `Rectangle(width=3.0, height=2.2, color=BLUE, fill_opacity=0.15).move_to(LEFT*3.2+DOWN*1.4)` |
| 12 | fade_in | `img_lbl` | 0.5 | `Text("2D Image", font_size=22, color=BLUE)`, `.move_to(LEFT*3.2+DOWN*1.4)` |
| 13 | create | `vid_group` | 1.0 | Four offset `Rectangle(width=2.6, height=1.9, color=GREEN, fill_opacity=0.1)` shifted at steps to mimic stacked frames, `VGroup(...).move_to(RIGHT*3.2+DOWN*1.4)` |
| 14 | fade_in | `vid_lbl` | 0.5 | `Text("3D Video\n(sequence of frames)", font_size=20, color=GREEN)`, `.next_to(vid_group, DOWN, buff=0.2)` |
| 15 | wait | — | 8.0 | — |
| 16 | highlight | `lbl_t2v` | 0.8 | `Indicate(lbl_t2v, color=YELLOW, scale_factor=1.15)` |
| 17 | wait | — | 3.0 | — |
| 18 | fade_out | `VGroup(header,divider,lbl_t2i,lbl_t2v,text_box_i,text_lbl_i,text_box_v,text_lbl_v,arr_i,arr_v,img_box,img_lbl,vid_group,vid_lbl)` | 1.0 | — |

**Layout:**
```
y= 3.0  header
y= 2.0  lbl_t2i (left) / lbl_t2v (right)
y= 1.0  text prompt boxes
y= 0.4→-0.2  arrows
y=-1.4  image box (left) / stacked video frames (right)
y=-2.8  vid_lbl
x=  0   divider
x=-3.2  left column (T2I)
x= 3.2  right column (T2V)
```

---

## SCENE 4 — 2D to 3D: Sequence of Frames
**Class:** `Scene4` · **Target:** 45s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("From 2D to 3D Output", font_size=44, color=WHITE)`, position=UP*3.0 |
| 2 | create | `single_frame` | 0.8 | `Rectangle(width=3.0, height=2.2, color=BLUE, fill_opacity=0.2).move_to(LEFT*3.5)` |
| 3 | fade_in | `lbl_2d` | 0.5 | `Text("2D Image", font_size=26, color=BLUE)`, `.next_to(single_frame, DOWN, buff=0.3)` |
| 4 | fade_in | `dim_lbl` | 0.5 | `Text("H × W × C", font_size=22, color=WHITE)`, `.move_to(single_frame)` |
| 5 | fade_in | `arrow_expand` | 0.8 | `Text("×16 frames", font_size=28, color=YELLOW)`, position=ORIGIN |
| 6 | fade_in | `arr_right` | 0.5 | `Arrow(LEFT*1.5, RIGHT*0.8, color=WHITE, stroke_width=3)` |
| 7 | create | `frames` | 1.2 | `VGroup` of 5 `Rectangle(width=2.4, height=1.8, color=GREEN, fill_opacity=0.12)` offset by `RIGHT*0.18+DOWN*0.15` each, `.move_to(RIGHT*3.5)` |
| 8 | fade_in | `lbl_3d` | 0.5 | `Text("3D Video", font_size=26, color=GREEN)`, `.next_to(frames, DOWN, buff=0.3)` |
| 9 | fade_in | `dim_lbl_3d` | 0.5 | `Text("T × H × W × C", font_size=22, color=WHITE)`, `.move_to(frames)` |
| 10 | wait | — | 8.0 | — |
| 11 | fade_in | `note` | 0.8 | `Text("New challenge: model must learn temporal coherence", font_size=24, color=YELLOW)`, position=DOWN*2.8 |
| 12 | wait | — | 5.0 | — |
| 13 | fade_out | `VGroup(header,single_frame,lbl_2d,dim_lbl,arrow_expand,arr_right,frames,lbl_3d,dim_lbl_3d,note)` | 1.0 | — |

**Layout:**
```
y= 3.0  header
y= 0.0  single_frame (left -3.5) / arrow / frames (right +3.5)
y=-0.9  labels (2D / ×16 / 3D)
y=-1.5  dimension labels
y=-2.8  note
```

---

## SCENE 5 — 3D Convolutions (C3D)
**Class:** `Scene5` · **Target:** 50s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("Handling Video: 3D Convolutions", font_size=40, color=WHITE)`, position=UP*3.0 |
| 2 | fade_in | `ref` | 0.5 | `Text("Tran et al., C3D — ICCV 2015", font_size=18, color=WHITE).set_opacity(0.6)`, position=UP*2.4 |
| 3 | fade_in | `lbl_2d_conv` | 0.6 | `Text("2D Conv", font_size=30, color=BLUE)`, position=LEFT*3.5+UP*0.8 |
| 4 | create | `kernel_2d` | 0.8 | `VGroup` of 9 `Square(side_length=0.55, color=BLUE, fill_opacity=0.3)` in 3×3 grid, `.move_to(LEFT*3.5+DOWN*0.3)` |
| 5 | fade_in | `size_2d` | 0.5 | `MathTex(r"3 \times 3", font_size=28, color=BLUE)`, `.next_to(kernel_2d, DOWN, buff=0.3)` |
| 6 | fade_in | `arr_extend` | 0.8 | `Arrow(LEFT*1.2, RIGHT*0.8, color=WHITE, stroke_width=3)`, with `Text("extend\nto time", font_size=20, color=WHITE).next_to(arr_extend, UP, buff=0.2)` |
| 7 | fade_in | `lbl_3d_conv` | 0.6 | `Text("3D Conv", font_size=30, color=GREEN)`, position=RIGHT*3.5+UP*0.8 |
| 8 | create | `kernel_3d` | 1.0 | `VGroup` of three 3×3 grids of `Square(side_length=0.5, color=GREEN, fill_opacity=0.2)` offset in depth (shift RIGHT*0.15+DOWN*0.12 each layer), `.move_to(RIGHT*3.5+DOWN*0.3)` |
| 9 | fade_in | `size_3d` | 0.5 | `MathTex(r"3 \times 3 \times 3", font_size=28, color=GREEN)`, `.next_to(kernel_3d, DOWN, buff=0.3)` |
| 10 | fade_in | `dim_note` | 0.8 | `Text("Spatial dims (H,W) + Temporal dim (T)", font_size=24, color=WHITE)`, position=DOWN*2.5 |
| 11 | wait | — | 8.0 | — |
| 12 | fade_in | `cost_note` | 0.6 | `Text("Cost: 3× more parameters — expensive!", font_size=22, color=RED)`, position=DOWN*3.1 |
| 13 | wait | — | 5.0 | — |
| 14 | fade_out | `VGroup(header,ref,lbl_2d_conv,kernel_2d,size_2d,arr_extend,lbl_3d_conv,kernel_3d,size_3d,dim_note,cost_note)` | 1.0 | — |

**Layout:**
```
y= 3.0  header
y= 2.4  ref
y= 0.8  conv labels (left/right)
y=-0.3  kernel visuals
y=-1.2  size labels
y=-2.5  dim_note
y=-3.1  cost_note
x=-3.5  2D conv
x= 3.5  3D conv
```

---

## SCENE 6 — (2+1)D Convolutions
**Class:** `Scene6` · **Target:** 50s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("(2+1)D Convolutions", font_size=44, color=WHITE)`, position=UP*3.0 |
| 2 | fade_in | `ref` | 0.5 | `Text("Tran et al., CVPR 2018", font_size=18, color=WHITE).set_opacity(0.6)`, position=UP*2.4 |
| 3 | fade_in | `idea` | 0.6 | `Text("Factorize 3D conv into two steps:", font_size=28, color=WHITE)`, position=UP*1.6 |
| 4 | create | `box_spatial` | 0.8 | `Rectangle(width=3.2, height=1.0, color=BLUE, fill_opacity=0.2).move_to(LEFT*2.5+UP*0.3)` |
| 5 | fade_in | `lbl_spatial` | 0.5 | `Text("2D Spatial Conv\n(H × W)", font_size=22, color=BLUE)`, `.move_to(box_spatial)` |
| 6 | fade_in | `plus` | 0.4 | `Text("+", font_size=40, color=WHITE)`, position=UP*0.3 |
| 7 | create | `box_temporal` | 0.8 | `Rectangle(width=3.2, height=1.0, color=GREEN, fill_opacity=0.2).move_to(RIGHT*2.5+UP*0.3)` |
| 8 | fade_in | `lbl_temporal` | 0.5 | `Text("1D Temporal Conv\n(T)", font_size=22, color=GREEN)`, `.move_to(box_temporal)` |
| 9 | fade_in | `eq` | 1.0 | `MathTex(r"f_{(2+1)D} = f_{1D}^{T} \circ f_{2D}^{HW}", font_size=30, color=YELLOW)`, position=DOWN*1.0 |
| 10 | wait | — | 5.0 | — |
| 11 | fade_in | `benefit` | 0.8 | `Text("Benefit: captures temporal dynamics\nwith fewer parameters than full 3D conv", font_size=24, color=WHITE)`, position=DOWN*2.3 |
| 12 | wait | — | 8.0 | — |
| 13 | highlight | `box_temporal` | 0.8 | `Indicate(box_temporal, color=YELLOW, scale_factor=1.1)` |
| 14 | wait | — | 3.0 | — |
| 15 | fade_out | `VGroup(header,ref,idea,box_spatial,lbl_spatial,plus,box_temporal,lbl_temporal,eq,benefit)` | 1.0 | — |

**Layout:**
```
y= 3.0  header
y= 2.4  ref
y= 1.6  idea
y= 0.3  two boxes side by side
y=-1.0  equation
y=-2.3  benefit text
x=-2.5  spatial box
x= 0.0  plus sign
x= 2.5  temporal box
```

---

## SCENE 7 — Video Diffusion Models: Overview
**Class:** `Scene7` · **Target:** 45s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("First Video Diffusion Model", font_size=42, color=WHITE)`, position=UP*3.0 |
| 2 | fade_in | `ref` | 0.5 | `Text("Ho et al. — NeurIPS 2022", font_size=22, color=BLUE)`, position=UP*2.3 |
| 3 | fade_in | `milestone` | 0.8 | `Text("First diffusion model for video generation", font_size=28, color=YELLOW)`, position=UP*1.5 |
| 4 | create | `noise_to_vid` | 1.2 | Three `NoisySquare` at t_ratio=1.0, 0.5, 0.0 left to right, each `scale(0.8)`, placed at x=-4, 0, +4, y=0 |
| 5 | fade_in | `arr1` | 0.4 | `Arrow(LEFT*2.5, LEFT*0.8, color=WHITE, stroke_width=3)` |
| 6 | fade_in | `arr2` | 0.4 | `Arrow(RIGHT*0.8, RIGHT*2.5, color=WHITE, stroke_width=3)` |
| 7 | fade_in | `lbl_noise` | 0.4 | `Text("Noise", font_size=22, color=WHITE)`, `.next_to(noise_squares[0], DOWN, buff=0.3)` |
| 8 | fade_in | `lbl_mid` | 0.4 | `Text("Denoise", font_size=22, color=WHITE)`, `.next_to(noise_squares[1], DOWN, buff=0.3)` |
| 9 | fade_in | `lbl_vid` | 0.4 | `Text("Video", font_size=22, color=GREEN)`, `.next_to(noise_squares[2], DOWN, buff=0.3)` |
| 10 | fade_in | `spec` | 0.8 | `Text("16-frame videos · 64×64 resolution", font_size=24, color=WHITE)`, position=DOWN*2.5 |
| 11 | wait | — | 8.0 | — |
| 12 | fade_in | `key` | 0.6 | `Text("Key: extend 2D diffusion U-Net to 3D over space AND time", font_size=22, color=BLUE)`, position=DOWN*3.1 |
| 13 | wait | — | 4.0 | — |
| 14 | fade_out | `VGroup(header,ref,milestone,noise_to_vid,arr1,arr2,lbl_noise,lbl_mid,lbl_vid,spec,key)` | 1.0 | — |

**Layout:**
```
y= 3.0  header
y= 2.3  ref
y= 1.5  milestone
y= 0.0  NoisySquare trio
y=-0.9  labels (Noise / Denoise / Video)
y=-2.5  spec
y=-3.1  key note
```

---

## SCENE 8 — VDM: Space-Only 3D Conv
**Class:** `Scene8` · **Target:** 50s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("VDM Architecture: 3D U-Net", font_size=40, color=WHITE)`, position=UP*3.0 |
| 2 | fade_in | `idea_lbl` | 0.6 | `Text("Inflate 2D conv → space-only 3D conv", font_size=28, color=YELLOW)`, position=UP*2.1 |
| 3 | create | `box_2d` | 0.8 | `Rectangle(width=3.0, height=0.8, color=BLUE, fill_opacity=0.2).move_to(LEFT*2.8+UP*0.8)` |
| 4 | fade_in | `lbl_2d_k` | 0.5 | `MathTex(r"2D\text{ Conv: }3 \times 3", font_size=26, color=BLUE)`, `.move_to(box_2d)` |
| 5 | fade_in | `arr_inflate` | 0.5 | `Arrow(LEFT*0.8, RIGHT*0.8, color=WHITE, stroke_width=3).shift(UP*0.8)` |
| 6 | fade_in | `infl_lbl` | 0.4 | `Text("inflate", font_size=20, color=WHITE)`, `.next_to(arr_inflate, UP, buff=0.15)` |
| 7 | create | `box_3d` | 0.8 | `Rectangle(width=3.2, height=0.8, color=GREEN, fill_opacity=0.2).move_to(RIGHT*2.8+UP*0.8)` |
| 8 | fade_in | `lbl_3d_k` | 0.5 | `MathTex(r"3D\text{ Conv: }1 \times 3 \times 3", font_size=26, color=GREEN)`, `.move_to(box_3d)` |
| 9 | fade_in | `note1` | 0.8 | `Text("Kernel size 1 along time dim → space-only", font_size=22, color=WHITE)`, position=DOWN*0.3 |
| 10 | fade_in | `feat_2d` | 0.6 | `MathTex(r"H \times W \times C", font_size=24, color=BLUE)`, position=DOWN*1.2 |
| 11 | fade_in | `arr_feat` | 0.4 | `Arrow(DOWN*1.0, DOWN*1.8, color=WHITE, stroke_width=2)` |
| 12 | fade_in | `feat_3d` | 0.6 | `MathTex(r"T \times H \times W \times C", font_size=24, color=GREEN)`, position=DOWN*2.0 |
| 13 | wait | — | 8.0 | — |
| 14 | highlight | `box_3d` | 0.8 | `Indicate(box_3d, color=YELLOW, scale_factor=1.1)` |
| 15 | wait | — | 4.0 | — |
| 16 | fade_out | `VGroup(header,idea_lbl,box_2d,lbl_2d_k,arr_inflate,infl_lbl,box_3d,lbl_3d_k,note1,feat_2d,arr_feat,feat_3d)` | 1.0 | — |

**Layout:**
```
y= 3.0  header
y= 2.1  idea label
y= 0.8  conv boxes + arrow
y=-0.3  note1
y=-1.2  feat_2d
y=-2.0  feat_3d
x=-2.8  2D box
x= 2.8  3D box
```

---

## SCENE 9 — VDM: Temporal Attention
**Class:** `Scene9` · **Target:** 45s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("VDM: Temporal Attention Layer", font_size=40, color=WHITE)`, position=UP*3.0 |
| 2 | fade_in | `idea` | 0.6 | `Text("Attend across time, not just space", font_size=26, color=YELLOW)`, position=UP*2.2 |
| 3 | fade_in | `frame_lbl` | 0.5 | `Text("Frame sequence (16 frames):", font_size=24, color=WHITE)`, position=LEFT*3.5+UP*1.1 |
| 4 | create | `frames_row` | 1.0 | `VGroup` of 6 `Square(side_length=0.7, color=BLUE, fill_opacity=0.2)` arranged horizontally with buff=0.15, `.move_to(UP*0.1)` |
| 5 | fade_in | `dots` | 0.4 | `Text("···", font_size=28, color=WHITE)`, `.next_to(frames_row, RIGHT, buff=0.2)` |
| 6 | create | `spattn_arc` | 0.8 | `CurvedArrow` from frame[0].get_top() to frame[1].get_top() curving up, color=BLUE |
| 7 | fade_in | `spattn_lbl` | 0.5 | `Text("Spatial attn\n(within frame)", font_size=20, color=BLUE)`, position=UP*1.8 |
| 8 | create | `tattn_arc` | 0.8 | `CurvedArrow` from frame[0].get_bottom() to frame[3].get_bottom() curving down, color=GREEN |
| 9 | fade_in | `tattn_lbl` | 0.5 | `Text("Temporal attn\n(across frames per pixel)", font_size=20, color=GREEN)`, position=DOWN*1.8 |
| 10 | wait | — | 5.0 | — |
| 11 | fade_in | `key` | 0.8 | `Text("Temporal attention: spatial axes treated as batch\n→ each pixel attends across its 16 time steps", font_size=22, color=WHITE)`, position=DOWN*2.7 |
| 12 | wait | — | 5.0 | — |
| 13 | fade_out | `VGroup(header,idea,frame_lbl,frames_row,dots,spattn_arc,spattn_lbl,tattn_arc,tattn_lbl,key)` | 1.0 | — |

**Layout:**
```
y= 3.0  header
y= 2.2  idea
y= 1.1  frame_lbl (left-aligned)
y= 0.1  frames_row
y= 1.8  spattn_lbl
y=-1.8  tattn_lbl
y=-2.7  key note
```

---

## SCENE 10 — Make-A-Video: Introduction
**Class:** `Scene10` · **Target:** 40s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `title` | 0.8 | `Text("Make-A-Video", font_size=52, color=ORANGE)`, position=UP*1.5 |
| 2 | fade_in | `org` | 0.5 | `Text("Singer et al., Meta — arXiv 2022", font_size=24, color=WHITE).set_opacity(0.7)`, position=UP*0.6 |
| 3 | fade_in | `key_insight` | 1.0 | `Text("Key insight:", font_size=30, color=YELLOW)`, position=DOWN*0.3 |
| 4 | fade_in | `insight_body` | 1.0 | `Text("Generate videos without text-video training pairs!\nLeverage pretrained T2I knowledge.", font_size=26, color=WHITE)`, position=DOWN*1.2 |
| 5 | wait | — | 5.0 | — |
| 6 | create | `box_t2i` | 0.7 | `Rectangle(width=3.0, height=0.7, color=BLUE, fill_opacity=0.2).move_to(LEFT*2.5+DOWN*2.5)` |
| 7 | fade_in | `t2i_lbl` | 0.5 | `Text("T2I Model\n(pretrained)", font_size=20, color=BLUE)`, `.move_to(box_t2i)` |
| 8 | fade_in | `arr_lift` | 0.5 | `Arrow(LEFT*1.0+DOWN*2.5, RIGHT*1.0+DOWN*2.5, color=WHITE, stroke_width=3)` |
| 9 | create | `box_t2v` | 0.7 | `Rectangle(width=3.0, height=0.7, color=ORANGE, fill_opacity=0.2).move_to(RIGHT*2.5+DOWN*2.5)` |
| 10 | fade_in | `t2v_lbl` | 0.5 | `Text("T2V Model\n(temporal layers added)", font_size=20, color=ORANGE)`, `.move_to(box_t2v)` |
| 11 | wait | — | 5.0 | — |
| 12 | fade_out | `VGroup(title,org,key_insight,insight_body,box_t2i,t2i_lbl,arr_lift,box_t2v,t2v_lbl)` | 1.0 | — |

**Layout:**
```
y= 1.5  title
y= 0.6  org
y=-0.3  key_insight
y=-1.2  insight_body
y=-2.5  T2I → T2V pipeline boxes
x=-2.5  T2I box
x= 2.5  T2V box
```

---

## SCENE 11 — Make-A-Video: Cascaded Pipeline
**Class:** `Scene11` · **Target:** 55s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("Make-A-Video: Cascaded Generation", font_size=38, color=WHITE)`, position=UP*3.0 |
| 2 | fade_in | `input_lbl` | 0.6 | `Text("Text\nPrompt", font_size=20, color=WHITE)`, position=LEFT*5.8+UP*0.0 |
| 3 | create | `box_clip` | 0.7 | `Rectangle(width=1.8, height=0.7, color=BLUE, fill_opacity=0.25).move_to(LEFT*3.8+UP*0.8)` |
| 4 | fade_in | `lbl_clip` | 0.4 | `Text("CLIP\nEmbed", font_size=16, color=BLUE)`, `.move_to(box_clip)` |
| 5 | create | `box_prior` | 0.7 | `Rectangle(width=1.8, height=0.7, color=BLUE, fill_opacity=0.25).move_to(LEFT*3.8+DOWN*0.2)` |
| 6 | fade_in | `lbl_prior` | 0.4 | `Text("ST Prior", font_size=16, color=BLUE)`, `.move_to(box_prior)` |
| 7 | fade_in | `out1_lbl` | 0.5 | `Text("16fr\n64×64", font_size=16, color=WHITE)`, position=LEFT*1.8+UP*0.3 |
| 8 | create | `box_dec` | 0.7 | `Rectangle(width=1.8, height=0.7, color=GREEN, fill_opacity=0.25).move_to(LEFT*0.0+UP*0.3)` |
| 9 | fade_in | `lbl_dec` | 0.4 | `Text("ST\nDecoder", font_size=16, color=GREEN)`, `.move_to(box_dec)` |
| 10 | fade_in | `out2_lbl` | 0.5 | `Text("76fr\n64×64", font_size=16, color=WHITE)`, position=RIGHT*1.9+UP*0.3 |
| 11 | create | `box_interp` | 0.7 | `Rectangle(width=1.8, height=0.7, color=YELLOW, fill_opacity=0.25).move_to(RIGHT*3.7+UP*0.3)` |
| 12 | fade_in | `lbl_interp` | 0.4 | `Text("Frame\nInterp", font_size=16, color=YELLOW)`, `.move_to(box_interp)` |
| 13 | fade_in | `out3_lbl` | 0.5 | `Text("76fr\n256×256", font_size=16, color=WHITE)`, position=RIGHT*3.7+DOWN*1.0 |
| 14 | create | `box_sr1` | 0.7 | `Rectangle(width=1.8, height=0.7, color=ORANGE, fill_opacity=0.25).move_to(LEFT*0.0+DOWN*2.2)` |
| 15 | fade_in | `lbl_sr1` | 0.4 | `Text("ST Super-Res", font_size=16, color=ORANGE)`, `.move_to(box_sr1)` |
| 16 | create | `box_sr2` | 0.7 | `Rectangle(width=1.8, height=0.7, color=RED, fill_opacity=0.25).move_to(RIGHT*3.7+DOWN*2.2)` |
| 17 | fade_in | `lbl_sr2` | 0.4 | `Text("Spatial\nSuper-Res", font_size=16, color=RED)`, `.move_to(box_sr2)` |
| 18 | fade_in | `final_lbl` | 0.6 | `Text("76fr · 768×768", font_size=18, color=WHITE)`, position=RIGHT*5.8+DOWN*2.2 |
| 19 | fade_in | `arrows_all` | 1.0 | `Arrow` connecting each stage left to right in order, `stroke_width=2, color=WHITE` |
| 20 | wait | — | 10.0 | — |
| 21 | fade_in | `note` | 0.6 | `Text("4 stages: each trained on images first, then video", font_size=22, color=YELLOW)`, position=DOWN*3.1 |
| 22 | wait | — | 5.0 | — |
| 23 | fade_out | `VGroup(...)` | 1.0 | all objects |

**Layout:**
```
y= 3.0  header
y= 0.8  CLIP embed + ST Prior (left cluster)
y= 0.3  ST Decoder / Frame Interp (middle)
y=-2.2  ST Super-Res / Spatial Super-Res (bottom)
y=-3.1  note
x=-5.8  text input
x=-3.8  prior boxes
x= 0.0  decoder
x= 3.7  interp / final SR
x= 5.8  final label
```

---

## SCENE 12 — Pseudo-3D Convolution Detail
**Class:** `Scene12` · **Target:** 55s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("Make-A-Video: Pseudo-3D Convolution", font_size=36, color=WHITE)`, position=UP*3.0 |
| 2 | fade_in | `paradigm` | 0.6 | `Text("Follows (2+1)D paradigm", font_size=26, color=YELLOW)`, position=UP*2.2 |
| 3 | create | `box_spatial_c` | 0.8 | `Rectangle(width=3.5, height=1.2, color=BLUE, fill_opacity=0.2).move_to(LEFT*2.5+UP*0.5)` |
| 4 | fade_in | `lbl_sc` | 0.6 | `Text("Spatial 2D Conv\n(pretrained T2I weights)", font_size=20, color=BLUE)`, `.move_to(box_spatial_c)` |
| 5 | fade_in | `plus_c` | 0.4 | `Text("+", font_size=36, color=WHITE)`, position=UP*0.5 |
| 6 | create | `box_temp_c` | 0.8 | `Rectangle(width=3.5, height=1.2, color=GREEN, fill_opacity=0.2).move_to(RIGHT*2.5+UP*0.5)` |
| 7 | fade_in | `lbl_tc` | 0.6 | `Text("Temporal 1D Conv\n(identity init)", font_size=20, color=GREEN)`, `.move_to(box_temp_c)` |
| 8 | fade_in | `init_detail` | 0.8 | `Text("Identity init:", font_size=24, color=WHITE)`, position=DOWN*0.8 |
| 9 | fade_in | `init_eq` | 1.0 | `MathTex(r"0 \cdot f_{prev} + 1 \cdot f_{curr} + 0 \cdot f_{next}", font_size=28, color=GREEN)`, position=DOWN*1.6 |
| 10 | wait | — | 5.0 | — |
| 11 | fade_in | `init_meaning` | 0.8 | `Text("→ at init, temporal conv copies current frame\n(same as no temporal mixing)", font_size=22, color=WHITE)`, position=DOWN*2.5 |
| 12 | wait | — | 8.0 | — |
| 13 | highlight | `lbl_tc` | 0.8 | `Indicate(box_temp_c, color=YELLOW, scale_factor=1.08)` |
| 14 | wait | — | 5.0 | — |
| 15 | fade_in | `benefit` | 0.6 | `Text("Pretrained T2I intact → stable finetuning start", font_size=22, color=YELLOW)`, position=DOWN*3.1 |
| 16 | wait | — | 3.0 | — |
| 17 | fade_out | `VGroup(...)` | 1.0 | all objects |

**Layout:**
```
y= 3.0  header
y= 2.2  paradigm
y= 0.5  two conv boxes
y=-0.8  init_detail
y=-1.6  init_eq
y=-2.5  init_meaning
y=-3.1  benefit
x=-2.5  spatial box
x= 0.0  plus
x= 2.5  temporal box
```

---

## SCENE 13 — Make-A-Video: Attention Layer Initialization
**Class:** `Scene13` · **Target:** 50s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("Make-A-Video: Attention Layers", font_size=40, color=WHITE)`, position=UP*3.0 |
| 2 | create | `box_sa` | 0.8 | `Rectangle(width=3.5, height=1.3, color=BLUE, fill_opacity=0.2).move_to(LEFT*2.5+UP*0.8)` |
| 3 | fade_in | `lbl_sa` | 0.6 | `Text("Spatial Attention\n(pretrained T2I weights)", font_size=20, color=BLUE)`, `.move_to(box_sa)` |
| 4 | fade_in | `sa_note` | 0.5 | `Text("Applied per-frame\nindependently", font_size=18, color=WHITE)`, `.next_to(box_sa, DOWN, buff=0.2)` |
| 5 | create | `box_ta` | 0.8 | `Rectangle(width=3.5, height=1.3, color=GREEN, fill_opacity=0.2).move_to(RIGHT*2.5+UP*0.8)` |
| 6 | fade_in | `lbl_ta` | 0.6 | `Text("Temporal Attention\n(zero initialized)", font_size=20, color=GREEN)`, `.move_to(box_ta)` |
| 7 | fade_in | `ta_note` | 0.5 | `Text("Learns dynamics\nacross time steps", font_size=18, color=WHITE)`, `.next_to(box_ta, DOWN, buff=0.2)` |
| 8 | fade_in | `zero_meaning` | 1.0 | `Text("Zero init → identity at start\n(output = spatial attn output only initially)", font_size=22, color=YELLOW)`, position=DOWN*2.0 |
| 9 | wait | — | 8.0 | — |
| 10 | fade_in | `summary` | 0.8 | `Text("Both spatial and temporal info captured\nwhile preserving T2I prior", font_size=22, color=WHITE)`, position=DOWN*3.0 |
| 11 | wait | — | 5.0 | — |
| 12 | fade_out | `VGroup(...)` | 1.0 | all objects |

**Layout:**
```
y= 3.0  header
y= 0.8  attention boxes
y=-0.3  per-box notes
y=-2.0  zero_meaning
y=-3.0  summary
x=-2.5  spatial attn
x= 2.5  temporal attn
```

---

## SCENE 14 — Make-A-Video: Training Strategy
**Class:** `Scene14` · **Target:** 45s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("Make-A-Video: Training Strategy", font_size=40, color=WHITE)`, position=UP*3.0 |
| 2 | fade_in | `sub` | 0.5 | `Text("4 networks, 2-phase training", font_size=26, color=YELLOW)`, position=UP*2.2 |
| 3 | create | `box1` | 0.7 | `Rectangle(width=4.0, height=0.7, color=BLUE, fill_opacity=0.2).move_to(UP*1.2)` |
| 4 | fade_in | `lbl1` | 0.5 | `Text("Phase 1: Train all 4 networks on image data", font_size=20, color=BLUE)`, `.move_to(box1)` |
| 5 | fade_in | `arr12` | 0.4 | `Arrow(UP*0.7, UP*0.1, color=WHITE, stroke_width=2)` |
| 6 | create | `box2` | 0.7 | `Rectangle(width=4.0, height=0.7, color=GREEN, fill_opacity=0.2).move_to(DOWN*0.2)` |
| 7 | fade_in | `lbl2` | 0.5 | `Text("Phase 2: Insert temporal layers, finetune on video", font_size=20, color=GREEN)`, `.move_to(box2)` |
| 8 | fade_in | `arr23` | 0.4 | `Arrow(DOWN*0.7, DOWN*1.3, color=WHITE, stroke_width=2)` |
| 9 | create | `box3` | 0.7 | `Rectangle(width=4.0, height=0.7, color=ORANGE, fill_opacity=0.2).move_to(DOWN*1.7)` |
| 10 | fade_in | `lbl3` | 0.5 | `Text("Data: WebVid-10M + 10M HD-VILA subset", font_size=20, color=ORANGE)`, `.move_to(box3)` |
| 11 | wait | — | 8.0 | — |
| 12 | fade_in | `note` | 0.6 | `Text("Spatial weights frozen during video finetuning\n→ preserves image quality", font_size=22, color=WHITE)`, position=DOWN*2.8 |
| 13 | wait | — | 5.0 | — |
| 14 | fade_out | `VGroup(...)` | 1.0 | all objects |

**Layout:**
```
y= 3.0  header
y= 2.2  sub
y= 1.2  box1 (Phase 1)
y= 0.7→0.1  arrow
y=-0.2  box2 (Phase 2)
y=-0.7→-1.3  arrow
y=-1.7  box3 (Data)
y=-2.8  note
```

---

## SCENE 15 — WebVid-10M Dataset
**Class:** `Scene15` · **Target:** 40s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("WebVid-10M Dataset", font_size=44, color=WHITE)`, position=UP*3.0 |
| 2 | fade_in | `ref` | 0.5 | `Text("Bain et al., ICCV 2021", font_size=20, color=WHITE).set_opacity(0.6)`, position=UP*2.3 |
| 3 | create | `stat_box` | 0.8 | `Rectangle(width=4.5, height=1.0, color=BLUE, fill_opacity=0.2).move_to(UP*1.0)` |
| 4 | fade_in | `stat_lbl` | 0.6 | `Text("10 million video-caption pairs", font_size=28, color=BLUE)`, `.move_to(stat_box)` |
| 5 | fade_in | `pair_demo` | 1.0 | Three `VGroup` each containing a `Rectangle(width=2.0, height=1.4, color=GREEN, fill_opacity=0.15)` + `Text("caption...", font_size=14, color=WHITE)` below, spaced horizontally, `.move_to(DOWN*0.5)` |
| 6 | wait | — | 5.0 | — |
| 7 | fade_in | `use_note` | 0.8 | `Text("Used to teach temporal dynamics\nSpatial quality from image pretraining", font_size=22, color=WHITE)`, position=DOWN*2.3 |
| 8 | wait | — | 5.0 | — |
| 9 | fade_out | `VGroup(...)` | 1.0 | all objects |

**Layout:**
```
y= 3.0  header
y= 2.3  ref
y= 1.0  stat_box
y=-0.5  video-caption demo
y=-2.3  use_note
```

---

## SCENE 16 — Make-A-Video: Evaluation
**Class:** `Scene16` · **Target:** 45s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("Make-A-Video: Evaluation", font_size=44, color=WHITE)`, position=UP*3.0 |
| 2 | fade_in | `metrics_lbl` | 0.6 | `Text("Key metrics:", font_size=28, color=YELLOW)`, position=UP*2.0 |
| 3 | create | `box_fid` | 0.7 | `Rectangle(width=3.0, height=0.8, color=BLUE, fill_opacity=0.2).move_to(LEFT*2.8+UP*1.0)` |
| 4 | fade_in | `lbl_fid` | 0.5 | `Text("FVD\n(video quality)", font_size=20, color=BLUE)`, `.move_to(box_fid)` |
| 5 | create | `box_clip` | 0.7 | `Rectangle(width=3.0, height=0.8, color=GREEN, fill_opacity=0.2).move_to(RIGHT*2.8+UP*1.0)` |
| 6 | fade_in | `lbl_clip_s` | 0.5 | `Text("CLIP Similarity\n(text-video align)", font_size=20, color=GREEN)`, `.move_to(box_clip)` |
| 7 | fade_in | `bar_group` | 1.2 | Simple bar chart: two bars (Previous SOTA vs Make-A-Video), FVD lower is better, CLIP higher is better. Bars as `Rectangle`, labels below. `.move_to(DOWN*0.8)` |
| 8 | wait | — | 5.0 | — |
| 9 | fade_in | `human_note` | 0.8 | `Text("Human evaluation: preferred Make-A-Video\nover previous models in both quality & alignment", font_size=22, color=WHITE)`, position=DOWN*2.6 |
| 10 | wait | — | 5.0 | — |
| 11 | fade_out | `VGroup(...)` | 1.0 | all objects |

**Layout:**
```
y= 3.0  header
y= 2.0  metrics_lbl
y= 1.0  metric boxes (FVD left, CLIP right)
y=-0.8  bar chart
y=-2.6  human_note
```

---

## SCENE 17 — Make-A-Video: Image Interpolation
**Class:** `Scene17` · **Target:** 40s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("Make-A-Video: Image Interpolation", font_size=38, color=WHITE)`, position=UP*3.0 |
| 2 | fade_in | `idea` | 0.6 | `Text("Given two images → generate in-between frames", font_size=26, color=YELLOW)`, position=UP*2.1 |
| 3 | create | `img_a` | 0.7 | `Rectangle(width=2.2, height=1.8, color=BLUE, fill_opacity=0.3).move_to(LEFT*4.0+UP*0.0)` |
| 4 | fade_in | `lbl_a` | 0.4 | `Text("Image A", font_size=20, color=BLUE)`, `.next_to(img_a, DOWN, buff=0.2)` |
| 5 | fade_in | `dots_frames` | 1.0 | Four `Rectangle(width=1.6, height=1.4, color=WHITE, fill_opacity=0.1, stroke_opacity=0.4)` between img_a and img_b, with dashed-style border (use `stroke_width=1`), positioned evenly from x=-1.5 to x=1.5 |
| 6 | fade_in | `gen_lbl` | 0.5 | `Text("Generated", font_size=18, color=WHITE).set_opacity(0.7)`, position=UP*0.0+DOWN*1.3 |
| 7 | create | `img_b` | 0.7 | `Rectangle(width=2.2, height=1.8, color=GREEN, fill_opacity=0.3).move_to(RIGHT*4.0+UP*0.0)` |
| 8 | fade_in | `lbl_b` | 0.4 | `Text("Image B", font_size=20, color=GREEN)`, `.next_to(img_b, DOWN, buff=0.2)` |
| 9 | wait | — | 5.0 | — |
| 10 | fade_in | `note` | 0.8 | `Text("Model learns motion and transitions\nbetween static images", font_size=22, color=WHITE)`, position=DOWN*2.5 |
| 11 | wait | — | 5.0 | — |
| 12 | fade_out | `VGroup(...)` | 1.0 | all objects |

**Layout:**
```
y= 3.0  header
y= 2.1  idea
y= 0.0  img_a | generated frames | img_b
y=-1.3  labels below frames
y=-2.5  note
```

---

## SCENE 18 — Imagen Video Overview
**Class:** `Scene18` · **Target:** 45s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("Imagen Video", font_size=48, color=WHITE)`, position=UP*2.5 |
| 2 | fade_in | `org` | 0.5 | `Text("Ho et al., Google — arXiv 2022", font_size=22, color=WHITE).set_opacity(0.7)`, position=UP*1.7 |
| 3 | fade_in | `similarity` | 0.8 | `Text("Similar to Make-A-Video:", font_size=26, color=YELLOW)`, position=UP*0.7 |
| 4 | fade_in | `point1` | 0.6 | `Text("• Built on Imagen T2I foundation model", font_size=24, color=WHITE)`, position=UP*0.0 |
| 5 | fade_in | `point2` | 0.6 | `Text("• Cascaded generation pipeline", font_size=24, color=WHITE)`, position=DOWN*0.6 |
| 6 | fade_in | `point3` | 0.6 | `Text("• Temporal layers added to pretrained weights", font_size=24, color=WHITE)`, position=DOWN*1.2 |
| 7 | wait | — | 5.0 | — |
| 8 | fade_in | `diff` | 0.8 | `Text("Key difference from Make-A-Video:\nUses text diffusion prior (Imagen) not CLIP", font_size=22, color=BLUE)`, position=DOWN*2.3 |
| 9 | wait | — | 8.0 | — |
| 10 | fade_out | `VGroup(...)` | 1.0 | all objects |

**Layout:**
```
y= 2.5  title
y= 1.7  org
y= 0.7  similarity label
y= 0.0  point1
y=-0.6  point2
y=-1.2  point3
y=-2.3  diff
```

---

## SCENE 19 — Align your Latents: Latent Diffusion
**Class:** `Scene19` · **Target:** 50s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("Align your Latents", font_size=48, color=WHITE)`, position=UP*2.8 |
| 2 | fade_in | `org` | 0.5 | `Text("Blattmann et al., Nvidia — CVPR 2023", font_size=22, color=WHITE).set_opacity(0.7)`, position=UP*2.1 |
| 3 | fade_in | `key_diff` | 0.8 | `Text("Key difference: operate in LATENT space", font_size=28, color=YELLOW)`, position=UP*1.3 |
| 4 | create | `box_pixel` | 0.7 | `Rectangle(width=3.2, height=0.8, color=RED, fill_opacity=0.2).move_to(LEFT*2.5+UP*0.2)` |
| 5 | fade_in | `lbl_pspace` | 0.5 | `Text("Pixel space diffusion\n(Make-A-Video, VDM)", font_size=19, color=RED)`, `.move_to(box_pixel)` |
| 6 | fade_in | `vs` | 0.4 | `Text("vs", font_size=30, color=WHITE)`, position=UP*0.2 |
| 7 | create | `box_latent` | 0.7 | `Rectangle(width=3.2, height=0.8, color=GREEN, fill_opacity=0.2).move_to(RIGHT*2.5+UP*0.2)` |
| 8 | fade_in | `lbl_lspace` | 0.5 | `Text("Latent space diffusion\n(Align your Latents)", font_size=19, color=GREEN)`, `.move_to(box_latent)` |
| 9 | fade_in | `benefit_lbl` | 0.8 | `Text("Latent space benefits:", font_size=24, color=WHITE)`, position=DOWN*0.9 |
| 10 | fade_in | `b1` | 0.5 | `Text("• Much smaller representation → faster", font_size=22, color=WHITE)`, position=DOWN*1.5 |
| 11 | fade_in | `b2` | 0.5 | `Text("• Leverages Stable Diffusion (LDM) pretrained weights", font_size=22, color=WHITE)`, position=DOWN*2.1 |
| 12 | wait | — | 8.0 | — |
| 13 | highlight | `box_latent` | 0.8 | `Indicate(box_latent, color=YELLOW, scale_factor=1.1)` |
| 14 | wait | — | 4.0 | — |
| 15 | fade_out | `VGroup(...)` | 1.0 | all objects |

**Layout:**
```
y= 2.8  header
y= 2.1  org
y= 1.3  key_diff
y= 0.2  pixel vs latent boxes
y=-0.9  benefit_lbl
y=-1.5  b1
y=-2.1  b2
```

---

## SCENE 20 — Align your Latents: Temporal Layer Insertion
**Class:** `Scene20` · **Target:** 45s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `header` | 0.8 | `Text("Align your Latents: Architecture", font_size=38, color=WHITE)`, position=UP*3.0 |
| 2 | fade_in | `base` | 0.6 | `Text("Base: Stable Diffusion LDM", font_size=26, color=YELLOW)`, position=UP*2.2 |
| 3 | create | `col1_box` | 0.7 | `Rectangle(width=3.0, height=0.8, color=BLUE, fill_opacity=0.2).move_to(LEFT*2.8+UP*1.0)` |
| 4 | fade_in | `col1_lbl` | 0.5 | `Text("Latent Diffusion\n+ Temporal Conv\n+ 3D Attention", font_size=18, color=BLUE)`, `.move_to(col1_box).scale(0.9)` |
| 5 | create | `col2_box` | 0.7 | `Rectangle(width=3.0, height=0.8, color=GREEN, fill_opacity=0.2).move_to(RIGHT*2.8+UP*1.0)` |
| 6 | fade_in | `col2_lbl` | 0.5 | `Text("Decoder\n+ 3D Conv layers\n(temporal consistency)", font_size=18, color=GREEN)`, `.move_to(col2_box).scale(0.9)` |
| 7 | fade_in | `arr_flow` | 0.8 | `Arrow(LEFT*0.8+UP*1.0, RIGHT*0.8+UP*1.0, color=WHITE, stroke_width=3)` |
| 8 | fade_in | `upsampler` | 0.6 | `Rectangle(width=3.0, height=0.7, color=ORANGE, fill_opacity=0.2).move_to(DOWN*0.2)` |
| 9 | fade_in | `up_lbl` | 0.5 | `Text("Upsampler + 3D Conv", font_size=20, color=ORANGE)`, `.move_to(upsampler)` |
| 10 | wait | — | 5.0 | — |
| 11 | fade_in | `compare` | 0.8 | `Text("Same idea as Make-A-Video,\nbut in compressed latent space → more efficient", font_size=22, color=WHITE)`, position=DOWN*1.5 |
| 12 | wait | — | 8.0 | — |
| 13 | fade_out | `VGroup(...)` | 1.0 | all objects |

**Layout:**
```
y= 3.0  header
y= 2.2  base label
y= 1.0  two boxes + arrow
y=-0.2  upsampler box
y=-1.5  compare text
```

---

## SCENE 21 — Summary & Outro
**Class:** `Scene21` · **Target:** 20s

| # | action_type | target | duration | parameters |
|---|---|---|---|---|
| 1 | fade_in | `title` | 0.8 | `Text("Section 2.1 — Key Takeaways", font_size=38, color=WHITE)`, position=UP*2.8 |
| 2 | fade_in | `t1` | 0.5 | `Text("1. T2V = extend T2I with temporal layers", font_size=24, color=BLUE)`, position=UP*1.5 |
| 3 | fade_in | `t2` | 0.5 | `Text("2. (2+1)D conv: efficient spatial+temporal factorization", font_size=24, color=GREEN)`, position=UP*0.7 |
| 4 | fade_in | `t3` | 0.5 | `Text("3. Cascaded pipelines: coarse → fine generation", font_size=24, color=YELLOW)`, position=DOWN*0.1 |
| 5 | fade_in | `t4` | 0.5 | `Text("4. Identity/zero init: stable finetuning from T2I", font_size=24, color=ORANGE)`, position=DOWN*0.9 |
| 6 | fade_in | `t5` | 0.5 | `Text("5. Latent space (Align your Latents) = faster + efficient", font_size=24, color=WHITE)`, position=DOWN*1.7 |
| 7 | wait | — | 5.0 | — |
| 8 | fade_out | `VGroup(title,t1,t2,t3,t4,t5)` | 2.0 | — |

**Layout:**
```
y= 2.8  title
y= 1.5  t1
y= 0.7  t2
y=-0.1  t3
y=-0.9  t4
y=-1.7  t5
```
