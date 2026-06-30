with open("data/raw/candidates.jsonl", "r") as infile:
    lines = infile.readlines()

with open("demo/sample_candidates.jsonl", "w") as outfile:
    outfile.writelines(lines[:100])

print("Created demo/sample_candidates.jsonl")