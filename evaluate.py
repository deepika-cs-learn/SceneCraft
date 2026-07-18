import json
import requests
from rouge_score import rouge_scorer

# Load the dataset
rows = []
with open("data/promptmax_train.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        rows.append(json.loads(line))

# Sample a subset to evaluate (last 50 rows)
sample = rows[-50:]

scorer = rouge_scorer.RougeScorer(["rougeL"], use_stemmer=True)
scores = []

print(f"Evaluating on {len(sample)} examples...\n")

for i, row in enumerate(sample):
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "scenecraft",
        "prompt": row["instruction"],
        "stream": False,
    })
    prediction = response.json()["response"]
    score = scorer.score(row["output"], prediction)["rougeL"].fmeasure
    scores.append(score)
    print(f"[{i+1}/{len(sample)}] ROUGE-L: {score:.3f}")

avg_score = sum(scores) / len(scores)
print(f"\nAverage ROUGE-L F1: {avg_score:.3f}")

# Save a report
with open("reports/evaluation.md", "w", encoding="utf-8") as f:
    f.write("# Evaluation\n\n")
    f.write(f"- Examples evaluated: {len(sample)}\n")
    f.write(f"- Average ROUGE-L F1: {avg_score:.3f}\n\n")
    f.write("**Note:** this evaluation was run on a sample from the training data itself, ")
    f.write("not a separate held-out test set — no test split was reserved before training. ")
    f.write("Treat this as a rough sanity check of output similarity, not a rigorous benchmark.\n")

print("\nSaved report to reports/evaluation.md")