import numpy as np

from scoring.semantic_score import calculate_semantic_scores


scores = calculate_semantic_scores()

print()

print("=" * 60)
print("Semantic Score Test")
print("=" * 60)

print("Candidates :", len(scores))
print()

print("Highest Score :", np.max(scores))
print("Lowest Score  :", np.min(scores))
print("Average Score :", np.mean(scores))