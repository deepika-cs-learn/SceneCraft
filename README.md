\# 🎨 SceneCraft



> A locally fine-tuned \*\*Qwen2.5-3B\*\* model that transforms short scene descriptions into rich, detailed prompts for AI image generation.



Built with \*\*QLoRA + Unsloth\*\*, exported directly to \*\*GGUF\*\*, and packaged for \*\*Ollama\*\*.



\---



\## ✨ Features



\- Convert simple image ideas into detailed generation prompts

\- Runs completely offline with Ollama

\- Fine-tuned on nearly \*\*1,800\*\* prompt-enhancement examples

\- Lightweight \*\*3B\*\* model suitable for local inference

\- Direct GGUF export using Unsloth (no manual llama.cpp pipeline)



\---



\## 🚀 Try it



Pull the model from Ollama:



```bash

ollama pull deepikagummallacs/scenecraft

```



Run it:



```bash

ollama run deepikagummallacs/scenecraft

```



\---



\## Example



\### Input



```text

a cat sitting on a windowsill

```



\### Output



```text

A white and black cat is sitting on a windowsill while gazing outside. Bright natural sunlight streams through the window, illuminating the cat's fur and creating soft shadows across the room. Its front paws rest gently on the sill while the background features a calm indoor setting with warm tones, producing a peaceful and cozy atmosphere...

```



\---



\# 🏗 Model Details



| Property | Value |

|-----------|-------|

| Base Model | Qwen2.5-3B-Instruct |

| Fine-tuning Method | QLoRA (4-bit) |

| Framework | Unsloth |

| Training Platform | Google Colab (Free T4 GPU) |

| Dataset | gokaygokay/prompt-enhancer-dataset |

| Training Samples | \~1,790 prompt pairs |

| Output Format | GGUF |

| Quantization | q4\_K\_M |

| Runtime | Ollama |



\---



\# 🛠 Training Pipeline



```text

Prompt Dataset

&#x20;     │

&#x20;     ▼

QLoRA Fine-tuning

&#x20;     │

&#x20;     ▼

Unsloth

&#x20;     │

&#x20;     ▼

Merge LoRA Weights

&#x20;     │

&#x20;     ▼

Export to GGUF

&#x20;     │

&#x20;     ▼

Quantize (Q4\_K\_M)

&#x20;     │

&#x20;     ▼

Ollama Model

```



Unlike the traditional llama.cpp workflow, \*\*Unsloth\*\* performs weight merging, GGUF conversion, and quantization in a single export step, allowing the entire project to be built within one Google Colab notebook.



\---



\# 📂 Repository Structure



```text

SceneCraft/

│

├── data/

│   └── promptmax\_train.jsonl

│

├── examples.md

│

├── Modelfile

│

├── SceneCraft\_Training.ipynb

│

└── README.md

```



\---



\# 📖 Dataset



Training data:



\*\*gokaygokay/prompt-enhancer-dataset\*\*



The dataset contains pairs of:



\- Short image descriptions

\- Rich, detailed image-generation prompts



Approximately \*\*1,790\*\* examples were used for fine-tuning.



\---



\# 💡 Use Cases



\- Stable Diffusion prompts

\- FLUX prompts

\- Midjourney prompts

\- DALL·E prompts

\- Leonardo AI

\- Ideogram

\- General prompt enhancement



\---



\# ⚠️ Limitations



\- Designed specifically for image-prompt expansion.

\- Not intended as a general-purpose instruction-following model.

\- May introduce plausible visual details (lighting, scenery, textures, objects) that were not explicitly mentioned in the original prompt.

\- No formal benchmark evaluation (ROUGE, BLEU, GPT-4 judging, etc.) has been performed yet.



\---



\# 📦 Model



Available on Ollama:



https://ollama.com/deepikagummallacs/scenecraft



\---



\# 🙏 Acknowledgements



\- Qwen Team

\- Unsloth

\- Ollama

\- Hugging Face

\- gokaygokay/prompt-enhancer-dataset



\---



\## ⭐ If you find this project useful, consider giving it a star!

