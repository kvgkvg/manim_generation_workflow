# VOICEOVER.md — Video Generation: Open-Source Base Models
Guide for recording. Use as reference, not word-for-word.

---

## SCENE 1 — Title Card (~8s)
[Title appears]: "In this section we look at open-source base models for video generation."

---

## SCENE 2 — Open-Source Motivation (~45s)
[Closed-source box]: "The pioneering video diffusion models we covered — from Google, Meta, and Nvidia — are all closed-source. This limits access for the broader research community."
[Arrow down]: "To address this, researchers began building and releasing open-source alternatives."
[Open-source box]: "Models like ModelScope, LaVie, and Stable Video Diffusion allow everyone to use, study, and build upon them."

---

## SCENE 3 — ModelScopeT2V Overview (~50s)
[Title]: "ModelScope Text-to-Video, from Wang et al. 2023, follows the same philosophy as the closed-source models: start from a strong pretrained image model and adapt it for video."
[Pipeline]: "They inflate Stable Diffusion to 3D — preserving all the pretrained weights — then insert spatio-temporal blocks to handle the time dimension."
[Bullets]: "Three core properties: preserving SD weights, spatio-temporal blocks, and crucially — the ability to handle a variable number of frames."

---

## SCENE 4 — ModelScopeT2V Architecture (~50s)
[Boxes]: "The architecture stacks on top of Stable Diffusion's latent diffusion backbone. The SD spatial convolutions keep their pretrained weights."
[New boxes]: "On top of those, new temporal convolution and temporal attention layers are inserted to handle the time dimension."
[Note]: "This is the same (2+1)D factorization pattern we saw before — proven effective, now in an open-source package."

---

## SCENE 5 — Variable-Length Sequences (~45s)
[Frames]: "One key design choice is that both the temporal conv and attention layers support variable sequence lengths. You're not fixed to 16 frames or 76 frames."
[Benefit]: "This flexibility is critical because it enables a dual-purpose model — set T to any video length for video, or set T to one for images."

---

## SCENE 6 — T=1 Dual Training (~45s)
[Two boxes]: "When the temporal length is set to one, the temporal layers have no effect — they just pass through. The model behaves identically to a standard image generation model."
[Same model]: "This means one model can handle both: train on large image datasets where T equals one, and on video data where T is greater than one."
[Benefit]: "This dramatically improves generalization — the model benefits from both the scale of image data and the temporal information from video."

---

## SCENE 7 — ZeroScope (~40s)
[Problem]: "One practical issue with ModelScope is that its training data — WebVid — contains Shutterstock watermarks, which appear in the generated videos."
[Fix]: "ZeroScope addresses this by finetuning ModelScope on a smaller, curated, watermark-free dataset."
[Result]: "The result: cleaner outputs at 1024 by 576 resolution, making it much more usable for real applications."

---

## SCENE 8 — Show-1 Text Alignment (~45s)
[Problem]: "Show-1 from Zhang et al. identifies a key weakness in latent-based video models: text alignment."
[Example]: "The example shown is: generate a panda by a waterfall holding a sign that says 'Show Lab'. Both ModelScope and commercial models like Gen-2 fail to render the sign correctly."
[Question]: "Why? Because in latent space, the compressed representation loses fine-grained detail — including text."

---

## SCENE 9 — Pixel vs Latent (~50s)
[Left box]: "Pixel-based diffusion models operate directly on image pixels. This gives them excellent text alignment and fine detail — but requires enormous memory at high resolution."
[Right box]: "Latent-based models work in the compressed latent space, which is much more memory-efficient — but this compression hurts text alignment, especially at low resolution."
[Solution]: "Show-1's insight: why choose one? Use pixel models where alignment matters most, and latent models where memory would be prohibitive."

---

## SCENE 10 — Show-1 Hybrid Pipeline (~50s)
[Pipeline]: "The Show-1 pipeline is cascaded. First, a pixel-based VDM generates low-resolution keyframes — alignment is critical here and memory is manageable at low res."
[Boxes]: "A pixel-based interpolation network then fills in the between frames."
[SR box]: "The final super-resolution stage switches to a latent-based model — because applying a pixel model at full resolution would run out of memory."
[Key]: "The hybrid gets the best of both: pixel's alignment strength at low-res, latent's efficiency at high-res."

---

## SCENE 11 — VideoCrafter (~40s)
[Title]: "VideoCrafter from Chen et al. takes a straightforward approach: latent diffusion with temporal layers inserted."
[Architecture]: "Same pattern: Stable Diffusion backbone, temporal convolutions, temporal attention."
[Note]: "Very similar to Align your Latents conceptually, but released as a high-quality open-source model."

---

## SCENE 12 — LaVie (~45s)
[Key]: "LaVie from NTU focuses on a different angle: the quality of training data."
[Dataset]: "They built Vimeo25M — 25 million high-quality video-text pairs, more than double WebVid's 10 million."
[Result]: "Higher quality data leads to noticeably better generation quality and resolution. Architecture-wise, it's a cascaded latent diffusion model."

---

## SCENE 13 — SVD Data Curation (~50s)
[Title]: "Stable Video Diffusion from Stability AI takes data quality even further with a systematic curation pipeline."
[Steps]: "First, cut detection and clipping ensures each training clip is a single coherent shot."
[Step 2]: "Synthetic captioning uses CoCa, V-BLIP, and an LLM to generate detailed descriptions of each clip."
[Step 3]: "CLIP similarity and aesthetic scores filter out low-quality content."
[Filters]: "Two key filters: static scene filtering removes videos with little or no motion using optical flow; OCR detection removes clips with heavy on-screen text if your task doesn't need it."

---

## SCENE 14 — LVD Dataset (~40s)
[Row 1]: "The resulting Large Video Dataset — LVD — contains 580 million clips with over 200 years of total video."
[Row 2]: "They also release LVD-10M, a 10-million clip subset comparable to WebVid in size but higher quality."
[Row 3]: "After their full filtering pipeline, only 2 million clips — about 25% — remain in the highest-quality subset."
[Key]: "The result is clear: well-curated training data beats simply having more data."

---

## SCENE 15 — SVD Stages 1 & 2 (~45s)
[Stage 1]: "SVD follows the now-familiar pattern. Stage one: initialize from Stable Diffusion 2.1 and inflate the 2D model to 3D to handle video."
[Stage 2]: "Stage two: large-scale pretraining on the LVD dataset."
[Note]: "This is exactly the same recipe as ModelScope to ZeroScope — start broad on a large dataset, then refine. The innovation is in how carefully they curate that dataset."

---

## SCENE 16 — SVD Stage 3 (~40s)
[Box]: "Stage three fine-tunes the pretrained model on roughly one million high-quality clips at 576 by 1024 resolution."
[Capabilities]: "This produces four distinct capabilities: text-to-video, image-to-video, frame interpolation, and multi-view generation."
[Key]: "Importantly, the quality gains from data curation in stage two persist through the finetuning — good data has lasting impact."

---

## SCENE 17 — Summary (~20s)
[Takeaways]: "Five key takeaways from 2.2: open-source democratizes access; ModelScope's T=1 trick enables dual image-video training; Show-1 proves hybrid pixel-latent pipelines work; LaVie shows data quality matters; and SVD demonstrates systematic curation as a first-class contribution."

---

## Recording Tips
- Pause 0.5s after each element appears before speaking about it
- Pipeline diagrams: follow left-to-right with your voice
- For comparisons (pixel vs latent): contrast tone left vs right
- Target ~150 words/minute for technical sections
