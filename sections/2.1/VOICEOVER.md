# VOICEOVER.md — Video Generation: Pioneering Works
Guide for recording. Use as reference, not word-for-word script.

---

## SCENE 1 — Title Card (~8s)
[Title appears]: "In this section we cover the pioneering works in video generation using diffusion models."

---

## SCENE 2 — Field Taxonomy (~45s)
[Taxonomy appears]: "The video generation landscape broadly splits into two families: pixel-space models and latent-space models. Both often use cascaded pipelines. Today we focus on the foundational works from 2022 to 2023 — Video Diffusion Models, Make-A-Video, Imagen Video, and Align your Latents."

---

## SCENE 3 — T2I vs T2V (~50s)
[Left side appears]: "Text-to-image generation takes a text prompt and produces a single 2D image."
[Right side appears]: "Text-to-video extends this — same text prompt, but now we generate a 3D output: a sequence of 2D frames over time."
[Highlight T2V]: "This transition from 2D to 3D is the core challenge. The model must now ensure frames are temporally consistent — not just individually good."

---

## SCENE 4 — 2D to 3D (~45s)
[Single frame]: "A standard image is a 2D tensor: height by width by channels."
[Arrow and stack]: "A video is simply 16, or 76, or more such frames stacked along a new time dimension — giving us T by H by W by C."
[Note appears]: "The new challenge is that the model has to learn temporal coherence — the content needs to make sense not just per frame, but across frames."

---

## SCENE 5 — 3D Convolutions (~50s)
[2D kernel]: "In image models we use 2D convolutions with 3-by-3 kernels operating on spatial dimensions."
[3D kernel]: "For video, C3D from ICCV 2015 extended this to 3D: a 3-by-3-by-3 kernel that also operates along the time dimension."
[Cost note]: "The downside is cost — adding that temporal dimension triples the number of kernel weights. Researchers quickly looked for more efficient alternatives."

---

## SCENE 6 — (2+1)D Convolutions (~50s)
[Two boxes]: "The (2+1)D approach from CVPR 2018 factorizes the 3D conv into two sequential operations: first a 2D spatial convolution, then a 1D temporal convolution."
[Equation]: "Mathematically, the (2+1)D filter is the composition of a temporal 1D filter with a spatial 2D filter."
[Benefit]: "This factorization captures the same spatial-temporal information but with significantly fewer parameters — and it's what the early video diffusion models build upon."

---

## SCENE 7 — Video Diffusion Models Overview (~45s)
[NoisySquare trio]: "Ho et al. from Google published the first video diffusion model at NeurIPS 2022. They showed that a diffusion model could generate coherent 16-frame videos from pure noise."
[Key point]: "The core idea is straightforward: extend the 2D diffusion U-Net to 3D by factorizing over space and time. This was a landmark result, demonstrating diffusion's potential beyond images."

---

## SCENE 8 — VDM: Space-Only Conv (~50s)
[Kernel inflation]: "The 2D convolution kernel with size 3-by-3 gets inflated to a 3D kernel of size 1-by-3-by-3. The temporal dimension kernel size is set to one — meaning it's space-only."
[Feature dimensions]: "The feature tensors grow from H-by-W-by-C in image models to T-by-H-by-W-by-C for video."
[Highlight]: "This is sometimes called pseudo-3D because while the tensor is 3D, convolutions still only operate spatially."

---

## SCENE 9 — VDM: Temporal Attention (~45s)
[Frames row]: "On top of spatial attention, VDM inserts temporal attention layers. While spatial attention operates within each frame independently — "
[Temporal arc]: "— temporal attention attends across the time dimension. For each spatial position, the model looks at how that pixel evolves across all 16 frames."
[Key note]: "In implementation, the spatial axes are treated as batch dimensions during temporal attention. This lets the model capture temporal dynamics necessary for coherent motion."

---

## SCENE 10 — Make-A-Video Introduction (~40s)
[Title appears]: "Make-A-Video from Meta took a clever approach to the data problem."
[Key insight]: "Training video-text pairs are expensive and rare. Their insight was: we can learn WHAT things look like from image-text pairs, and learn HOW things move separately from unlabeled video data."
[T2I → T2V boxes]: "Start with a pretrained text-to-image model, then add and finetune temporal layers — without ever needing paired text-video training data."

---

## SCENE 11 — Cascaded Pipeline (~55s)
[Pipeline stages appear one by one]: "Make-A-Video uses a four-stage cascaded pipeline."
[Prior + decoder]: "First, a text input is encoded to a CLIP embedding. A spatiotemporal prior and decoder generate a very short, low-resolution 16-frame video at 64 by 64."
[Interpolation]: "A frame interpolation network extends this to 76 frames — increasing temporal duration."
[Super-resolution stages]: "Two super-resolution stages, one spatiotemporal and one spatial-only, progressively increase resolution to 256 and then 768."
[Note]: "Each of the four networks is first trained on images alone to give a stable initialization."

---

## SCENE 12 — Pseudo-3D Convolution (~55s)
[Two boxes]: "The convolution layers in Make-A-Video follow the (2+1)D paradigm: spatial 2D conv initialized from pretrained T2I weights, plus a temporal 1D conv."
[Identity init]: "The temporal conv is initialized to be an identity: it weights the previous frame at zero, the current frame at one, and the next frame at zero."
[Meaning]: "At initialization this means the temporal conv has no effect — the output is identical to what you'd get with no temporal mixing at all. This preserves the pretrained T2I behavior at the start of finetuning, giving a stable starting point."

---

## SCENE 13 — Attention Layer Initialization (~50s)
[Two boxes]: "The same strategy applies to attention layers. Spatial attention keeps the pretrained T2I weights and operates per-frame independently."
[Temporal attn]: "Temporal attention is newly inserted and initialized to zero — meaning its output is zero at initialization, so the overall block output equals the spatial attention output only."
[Summary]: "This zero-initialization trick ensures both spatial and temporal information can be learned while the pretrained knowledge of what things look like is fully preserved."

---

## SCENE 14 — Training Strategy (~45s)
[Phase 1]: "All four networks are first trained on image data — WebVid captions paired with single frames. This gives the temporal layers a good starting distribution."
[Phase 2]: "Then temporal layers are inserted and finetuned on video data. Spatial weights are kept frozen during video finetuning to prevent catastrophic forgetting."
[Data note]: "Training uses 10 million videos from WebVid-10M and 10 million clips from the HD-VILA dataset."

---

## SCENE 15 — WebVid-10M (~40s)
[Dataset stats]: "WebVid-10M, introduced by Bain et al. at ICCV 2021, contains 10 million video-caption pairs. Videos are high quality and come with descriptive captions."
[Use]: "This dataset teaches the model temporal dynamics — how objects and scenes change over time. The spatial quality comes from the image pretraining stage."

---

## SCENE 16 — Evaluation (~45s)
[Metrics]: "Make-A-Video is evaluated using FVD — Fréchet Video Distance, the video analog of FID — to measure generation quality, and CLIP similarity to measure text-video alignment."
[Bar chart]: "Make-A-Video showed significant improvements over previous state-of-the-art on both metrics."
[Human eval]: "Human evaluators also preferred Make-A-Video in both visual quality and text alignment when compared to prior models."

---

## SCENE 17 — Image Interpolation (~40s)
[Two images]: "One impressive capability of Make-A-Video is image interpolation. Given two input images A and B — "
[Generated frames]: "— the model generates the intermediate frames, animating a plausible transition between the two."
[Note]: "This demonstrates the model has learned genuine motion and scene dynamics, not just texture — it can reason about how a scene would evolve between two states."

---

## SCENE 18 — Imagen Video (~45s)
[Title]: "Google released Imagen Video concurrently with Make-A-Video, also in late 2022."
[Points]: "The high-level approach is very similar: build on a strong pretrained T2I model — in this case Imagen — use cascaded generation, and add temporal layers to the existing architecture."
[Difference]: "The key distinction is the foundation model. Imagen Video uses Imagen's text diffusion prior rather than CLIP embeddings."

---

## SCENE 19 — Align your Latents: Latent Space (~50s)
[Pixel vs latent]: "Align your Latents from Nvidia at CVPR 2023 takes a different approach. While Make-A-Video and VDM operate in pixel space — directly on raw video frames — Align your Latents operates in latent space."
[Benefits]: "The latent representation is much smaller than the full pixel resolution, making the diffusion process significantly faster. And it allows the model to leverage Stable Diffusion's pretrained weights directly."

---

## SCENE 20 — Align your Latents: Architecture (~45s)
[Boxes]: "The architecture inserts temporal convolutional and 3D attention layers into the latent diffusion model. The decoder is modified with 3D convolutional layers to preserve temporal consistency when decoding from latent to pixel space."
[Upsampler]: "An upsampler with 3D convolutions handles spatial super-resolution while maintaining temporal coherence."
[Compare]: "Same fundamental idea as Make-A-Video — but operating in compressed latent space makes the whole pipeline more computationally efficient."

---

## SCENE 21 — Summary (~20s)
[Takeaways appear]: "Five key ideas from section 2.1: text-to-video is text-to-image plus temporal layers; (2+1)D factorization efficiently captures both spatial and temporal structure; cascaded pipelines build quality progressively from coarse to fine; identity and zero initialization enable stable finetuning from pretrained image weights; and operating in latent space improves efficiency."

---

## Recording Tips
- Watch the full animation once before starting
- Pause 0.5s after each new element appears before speaking about it
- Equation scenes: name each term as it highlights
- Pipeline diagrams: follow the left-to-right flow with your voice
- Architecture boxes: describe left box first, then right
- Target pace: ~150 words/minute for technical content
