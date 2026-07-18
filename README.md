\# scenecraft



Turn a short image idea into a detailed, ready-to-use image-generation prompt.



\## Why this exists



Short prompts like "a dog in a park" often give weak, vague results in image generators. scenecraft expands them into rich descriptions — lighting, composition, background, texture — so the image model has more to work with.



\## Try it



`ollama run deepikagummallacs/scenecraft

`

\### Example:



> \*\*You type:\*\* a cat sitting on a windowsill

>

> \*\*It replies:\*\* A white and black cat is seen looking out of a window. The cat's front paws are resting upon the windowsill, while its hindquarters lean against the side of the window. A bright light shines onto the backside of the cat from outside the building. The floor below consists of dark brown hardwood flooring with two coffee cup lids on top of it.



\## Setup



1\. Install Ollama → \[ollama.com/download](https://ollama.com/download)

2\. Pull and rename for convenience:



```

ollama pull deepikagummallacs/scenecraft



ollama cp deepikagummallacs/scenecraft scenecraft

```



3\. Run it:



`ollama run scenecraft`



`/bye` to exit.



\## Calling it from code



```python

import requests



response = requests.post("http://localhost:11434/api/generate", json={

&#x20;   "model": "scenecraft",

&#x20;   "prompt": "a cat sitting on a windowsill",

&#x20;   "stream": False,

})

print(response.json()\["response"])

```



\## Under the hood



| | |

|---|---|

| Base model | Qwen2.5-3B-Instruct |

| Method | QLoRA (4-bit) fine-tuning via Unsloth |

| Data | \[gokaygokay/prompt-enhancer-dataset](https://huggingface.co/datasets/gokaygokay/prompt-enhancer-dataset) — \~1,790 short → detailed image prompt pairs |

| Trained on | Free Google Colab T4 GPU |

| Exported as | GGUF, q4\_K\_M quantization (\~1.9GB) |



\## Good to know



\- It's built for \*\*visual/scene prompts\*\* specifically — feeding it a coding question or essay topic won't work well, it'll try to describe it as a scene instead.

\- It tends to invent plausible visual details (lighting, background objects) that weren't in your original prompt — that's intentional, it's what makes the output richer, but don't expect it to stay strictly literal.

\- Best paired with image generators like Stable Diffusion, Midjourney, or Flux, where more descriptive prompts genuinely improve output quality.

\- Not evaluated with formal metrics (ROUGE-L etc.) yet — feedback on output quality is welcome via issues/comments.



\## Common issues



\*\*"model not found"\*\* → run `ollama pull deepikagummallacs/scenecraft` again, then re-run the `cp` command.



\*\*Want it gone\*\* → `ollama rm scenecraft`



\*\*Check what's installed\*\* → `ollama list`



\### \*\*What it is\*\*



\*\*Base model:\*\* Qwen2.5-3B-Instruct



\*\*Fine-tuning method:\*\* LoRA (QLoRA, 4-bit) via Unsloth



\*\*Training data:\*\* \~1,790 examples from gokaygokay/prompt-enhancer-dataset (short image caption → detailed visual description pairs)



\*\*Format:\*\* GGUF, quantized to q4\_K\_M (\~1.9GB) for fast local inference via Ollama



\*\*Runs on:\*\* CPU or GPU, no special hardware required to use it (a free Colab T4 GPU was used for training)

