\# scenecraft — Fine-Tuned Image Prompt Expansion Model



scenecraft is a locally fine-tuned language model designed to expand short image prompts into rich, detailed scene descriptions suitable for text-to-image generation models (Stable Diffusion, Midjourney-style prompts, etc.).



It is trained via QLoRA, exported to GGUF, and served through Ollama for zero-setup local use.



\------------------------------------------------------------



\## Overview



Base Model: unsloth/Qwen2.5-3B-Instruct  

Training Method: QLoRA (4-bit)  

Training Examples: 1,790 short → detailed prompt pairs  

GPU Used: Google Colab (Free T4)  

Export Format: GGUF (q4\_K\_M)  

Model Size: \~1.9GB  

Evaluation (Sanity Check): ROUGE-L F1 = 0.257  



Note: Evaluation was performed on a sample drawn from training data. This is a rough sanity check, not a rigorous benchmark.



\------------------------------------------------------------



\## Try It with Ollama (No Setup Required)



Run locally using:



ollama pull deepikagummallacs/scenecraft

ollama run deepikagummallacs/scenecraft



Model page:

https://ollama.com/deepikagummallacs/scenecraft



No Python, no GPU, no cloning required — only Ollama installed locally.



\------------------------------------------------------------



\## What scenecraft Does



Input:

a girl in a forest



Output:

A young girl standing in a dense emerald forest, soft golden sunlight filtering

through tall pine trees, gentle mist hovering above moss-covered ground,

cinematic lighting, ultra-detailed textures, shallow depth of field,

high-resolution, fantasy atmosphere.



The goal is creative scene enrichment, not literal rewriting.



It intentionally:

\- Adds lighting details

\- Introduces environmental context

\- Enhances atmosphere

\- Expands visual depth

\- Adds stylistic cues for generative art models



\------------------------------------------------------------



\## Full Training Pipeline



To retrain or modify the model:



git clone https://github.com/deepika-cs-learn/SceneCraft

cd SceneCraft



\------------------------------------------------------------



Phase 1 — Data Collection



Dataset used:

gokaygokay/prompt-enhancer-dataset (Hugging Face)



Contains 1,790 short-caption → detailed-description pairs.



Data was cleaned, deduplicated, and saved as:

data/promptmax\_train.jsonl



\------------------------------------------------------------



Phase 2 — Training Environment



Used Unsloth QLoRA Colab notebook.

Runtime: Free T4 GPU.

Training time: \~20–60 minutes for 3 epochs.



\------------------------------------------------------------



Phase 3 — Base Model + LoRA Configuration



Base model:

unsloth/Qwen2.5-3B-Instruct



Configuration:

\- 4-bit loading (QLoRA)

\- LoRA rank r = 16

\- Applied to attention and MLP projection layers



\------------------------------------------------------------



Phase 4 — Data Formatting



Each pair was formatted using the model's chat template:



System: You expand short image prompts into detailed scene descriptions.

User: a castle on a hill

Assistant: \[expanded output]



\------------------------------------------------------------



Phase 5 — QLoRA Training



\- 4-bit precision

\- 3 epochs

\- Free Colab T4 GPU

\- \~20–60 minutes total training



\------------------------------------------------------------



Phase 6 — Evaluation



Average ROUGE-L F1: 0.257



Important:

No held-out test split was used.

This is only a sanity check.



Evaluation files:

evaluate.py

reports/evaluation.md



\------------------------------------------------------------



Phase 7 — Merge + GGUF Export



Exported using Unsloth:



model.save\_pretrained\_gguf(

&#x20;   "scenecraft\_model",

&#x20;   tokenizer,

&#x20;   quantization\_method="q4\_k\_m"

)



This merges the LoRA adapter and exports directly to GGUF.

Final file size: \~1.9GB



\------------------------------------------------------------



Phase 8 — Ollama Packaging



ollama create scenecraft -f Modelfile

ollama run scenecraft



\------------------------------------------------------------



\## Requirements



To run:

\- Ollama installed locally



To retrain:

\- Google account (Colab GPU)

\- Hugging Face account

\- Basic Python knowledge



No local GPU required.



\------------------------------------------------------------



\## Limitations



\- Built specifically for visual/scene prompts.

\- Not designed for coding or general writing tasks.

\- May invent plausible visual details (lighting, textures, atmosphere).

\- Evaluation is not rigorous.



\------------------------------------------------------------



\## Intended Use Cases



\- Stable Diffusion prompt enhancement

\- Midjourney-style scene building

\- Creative concept art ideation

\- Game environment brainstorming

\- Storyboarding visual scene expansion



\------------------------------------------------------------



\## Summary



scenecraft demonstrates that domain-specific fine-tuning is possible on free GPUs using QLoRA and Unsloth, and can be deployed locally via GGUF and Ollama with zero setup.



Lightweight. Specialized. Fully local.

