\# scenecraft — Fine-Tuned Image Prompt Expansion Model



A locally fine-tuned language model, trained via QLoRA on short-to-detailed image prompt pairs, exported to GGUF, and served through Ollama (https://ollama.com/).



\- Base training examples: 1,790

\- Evaluation: ROUGE-L F1 = 0.257 (see caveat below)

\- Trained on: Google Colab (free T4 GPU)

\- Export format: GGUF, quantized to q4\_K\_M (\~1.9GB)



\## Try it with Ollama (no setup required)



`ollama pull deepikagummallacs/scenecraft

&#x20;ollama run deepikagummallacs/scenecraft

`



Model page: https://ollama.com/deepikagummallacs/scenecraft



See examples.md for a sample interaction.



\## Full Training Pipeline



If you want to retrain the model yourself, clone the repo:



`git clone https://github.com/deepika-cs-learn/SceneCraft

&#x20;cd SceneCraft

`



\*\*Phase 1 — Data Collection\*\*



Used the gokaygokay/prompt-enhancer-dataset from Hugging Face (https://huggingface.co/datasets/gokaygokay/prompt-enhancer-dataset) — 1,790 short-image-caption to detailed-description pairs, cleaned and deduplicated into data/promptmax\_train.jsonl.



\*\*Phase 2 — Training Setup\*\*



Opened the Unsloth Qwen2.5-3B Colab notebook and set the runtime to a T4 GPU.



\*\*Phase 3 — Load Base Model + LoRA Config\*\*



Loaded unsloth/Qwen2.5-3B-Instruct in 4-bit (QLoRA), with LoRA rank r = 16 applied to the attention and MLP projection layers.



\*\*Phase 4 — Format \& Load Data\*\*



Formatted each row using the model's chat template, with a system prompt describing the image-expansion task.



\*\*Phase 5 — QLoRA Training\*\*



Trained in 4-bit precision using QLoRA via Unsloth, for 3 epochs on the free Colab T4 GPU (roughly 20-60 minutes).



\*\*Phase 6 — Evaluation\*\*



Ran a ROUGE-L comparison between model outputs and reference outputs on a 50-example sample:## Calling it from code



\##Average ROUGE-L F1: 0.257



Important caveat: this was evaluated on a sample drawn from the training data itself, not a separate held-out test set — no test split was reserved before training. Treat this as a rough sanity check rather than a rigorous benchmark. Full script and output: evaluate.py and reports/evaluation.md.



\*\*Phase 7 — Merge + GGUF Export\*\*



Unlike a manual PEFT + llama.cpp pipeline, Unsloth merges the LoRA adapter into the base model and exports directly to GGUF in a single call:



`model.save\_pretrained\_gguf("scenecraft\_model", tokenizer, quantization\_method="q4\_k\_m")`





This produces a quantized .gguf file (\~1.9GB) with no separate merge or conversion script needed.



\*\*Phase 8 — Ollama Packaging \& Inference\*\*



Packaged the GGUF file into an Ollama model using a Modelfile:



`ollama create scenecraft -f Modelfile

ollama run scenecraft `



\## Requirements



Just want to run the model? All you need is Ollama (https://ollama.com/) installed locally — no Python, no GPU, no cloning required:



`ollama pull deepikagummallacs/scenecraft

ollama run deepikagummallacs/scenecraft `



Want to retrain or modify the pipeline yourself? You'll additionally need:



\- A Google account (for Colab's free GPU — no local GPU required)

\- A Hugging Face account (to load the dataset)



\## Limitations



\- Built for visual/scene prompts specifically — not general-purpose prompt improvement (coding, writing, analysis, etc.).

\- Tends to invent plausible visual details not present in the original short prompt (lighting, background objects) — intentional, since the goal is richer output, not literal expansion.

\- Evaluation is a rough sanity check (see Phase 6 caveat above), not a rigorous benchmark.

