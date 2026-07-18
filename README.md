\# scenecraft



A locally fine-tuned Qwen2.5-3B model that expands short image descriptions into detailed, ready-to-use image-generation prompts.



Model page: https://ollama.com/deepikagummallacs/scenecraft



\## Quick start



No training needed to use it — just Ollama:



\\`\\\\`\\`

ollama pull deepikagummallacs/scenecraft

ollama run deepikagummallacs/scenecraft

\\`\\\\`\\`



Example:

\\`\\\\`\\`

Input:  a cat sitting on a windowsill

Output: A white and black cat is seen looking out of a window. The cat's

front paws are resting upon the windowsill, while its hindquarters lean

against the side of the window. A bright light shines onto the backside

of the cat from outside the building...

\\`\\\\`\\`



\## How it was built



| | |

|---|---|

| Base model | Qwen2.5-3B-Instruct |

| Method | QLoRA (4-bit) fine-tuning via Unsloth (https://github.com/unslothai/unsloth) |

| Platform | Google Colab (free T4 GPU) |

| Dataset | gokaygokay/prompt-enhancer-dataset (https://huggingface.co/datasets/gokaygokay/prompt-enhancer-dataset) — \~1,790 short → detailed image-prompt pairs |

| Export | Direct GGUF export via Unsloth's save\_pretrained\_gguf, quantized to q4\_K\_M |



Unlike a manual llama.cpp export pipeline, Unsloth handles the merge, GGUF conversion, and quantization in a single function call, which is why this project has no separate merge/export scripts — it's a single Colab notebook end to end.



\## Files in this repo



\- data/promptmax\_train.jsonl — the cleaned training data (instruction/output pairs)

\- examples.md — a sample input/output interaction

\- Modelfile — the Ollama configuration used to package the GGUF into a runnable model



\## Limitations



\- Built for visual/scene prompts specifically — not general-purpose prompt improvement.

\- Tends to invent plausible visual details not present in the original short prompt (lighting, background objects) — intentional, since the goal is richer output, not literal expansion.

\- No formal quality benchmark run yet (e.g. ROUGE-L) — feedback welcome.

