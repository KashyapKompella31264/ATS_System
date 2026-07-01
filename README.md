# Intelligent Candidate Discovery & Ranking System

A semantic candidate ranking system developed for the **Intelligent Candidate Discovery & Ranking Challenge**. The system combines dense semantic retrieval with structured candidate evaluation to identify the most relevant candidates from a large candidate pool.

---

# Quick Start

## 1. Clone the Repository

```bash
git clone <repository-url>
cd candidate-ranking-system
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Build Docker Image (Optional)

```bash
docker build -t candidate-ranking-system .
```

---

## 4. Generate Embedding Artifacts (One-Time Preprocessing)

Run the following command by providing the path to the candidate dataset:

```bash
python -m src.features.embedding_generator --candidates <path_to_candidates.jsonl>
```

Example:

```bash
python -m src.features.embedding_generator --candidates data/raw/candidates.jsonl
```

This generates the following artifacts inside the `artifact/` directory:

```
candidate_general_embeddings.npy
candidate_career_embeddings.npy
candidate_skill_embeddings.npy
candidate_ids.npy
domain_embeddings.npy
domain_labels.json
jd_embedding.npy
```

---

## 5. Generate Final Ranking

Run the ranking pipeline by providing the path to the candidate dataset and the desired output location:

```bash
python -m rank --candidates <path_to_candidates.jsonl> 
    --out <output_submission.csv>
```

```bash
python -m rank --candidates data/raw/my_candidates.jsonl --out output/my_submission.csv   
```

The generated submission file will be available at

```
output/submission.csv
```

---

# Project Overview

The objective of this project is to rank candidates based on their suitability for a target AI/ML role.

Instead of relying solely on keyword matching, the system combines semantic retrieval with multiple structured scoring modules to evaluate candidate relevance.

The final ranking considers:

- Semantic relevance to the Job Description
- Career progression
- Product company experience
- Skill-career consistency
- Recruiter behavior signals
- Domain expertise
- Location preference

The system produces an explainable ranked list of the Top 100 candidates along with reasoning for each recommendation.

---

# Repository Structure

```
candidate-ranking-system/
│
├── artifact/
│   ├── candidate_general_embeddings.npy
│   ├── candidate_career_embeddings.npy
│   ├── candidate_skill_embeddings.npy
│   ├── candidate_ids.npy
│   ├── jd_embedding.npy
│   ├── domain_embeddings.npy
│   └── domain_labels.json
│
├── data/
│   └── raw/
│       ├── candidates.jsonl
│       └── jd.txt
│
├── src/
│   ├── features/
│   ├── parser/
│   ├── ranking/
│   ├── scoring/
│   └── utils/
│
├── tests/
│
├── embedding_generator.py
├── rank.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

# System Pipeline

```
Candidates
      │
      ▼
Structured Document Generation
      │
      ▼
Embedding Generation
      │
      ▼
Semantic Retrieval
      │
      ▼
Top-K Candidate Selection
      │
      ▼
Career Scoring
Behavior Scoring
Consistency Scoring
Domain Scoring
Location Scoring
      │
      ▼
Weighted Final Ranking
      │
      ▼
submission.csv
```

---

# Scoring Modules

| Module            | Description                                                                                                |
| ----------------- | ---------------------------------------------------------------------------------------------------------- |
| Semantic Score    | Measures semantic similarity between the candidate profile and the Job Description.                        |
| Career Score      | Evaluates years of experience, career progression, product company experience, and current role relevance. |
| Consistency Score | Measures alignment between candidate skills and career history.                                            |
| Behavior Score    | Uses recruiter engagement and platform activity signals.                                                   |
| Domain Score      | Measures similarity between candidate experience and target AI/ML domains.                                 |
| Location Score    | Rewards candidates matching preferred hiring locations or willing to relocate.                             |

---

# Final Scoring Formula

| Module            | Weight |
| ----------------- | -----: |
| Semantic Score    |    35% |
| Career Score      |    22% |
| Consistency Score |    15% |
| Behavior Score    |    13% |
| Domain Score      |    10% |
| Location Score    |     5% |

---

# Embedding Model

Sentence Transformer

```
all-MiniLM-L6-v2
```

All embeddings are generated using normalized vector representations.

---

# Candidate Representation

Each candidate is transformed into three structured textual representations:

- General Profile Document
- Career History Document
- Skill Profile Document

Separate embeddings are generated for each representation to support multiple scoring modules.

---

# Explainable Ranking

Each shortlisted candidate includes a generated explanation highlighting the strongest factors contributing to the recommendation.

Example:

```
Excellent semantic match with the job description, strong career progression, high recruiter engagement, and relevant product-company experience.
```

---

# Assumptions

- The candidate dataset used during ranking matches the dataset used during embedding generation.
- Candidate embeddings are precomputed before ranking.
- The Job Description is fixed according to the challenge specification.
- Ranking is deterministic.
- Candidates with identical scores are ordered by ascending Candidate ID.

---

# Technologies Used

- Python
- Sentence Transformers
- NumPy
- Pandas
- Scikit-learn

---

# Output Format

The generated submission file contains the following columns:

| Column       |
| ------------ |
| candidate_id |
| rank         |
| score        |
| reasoning    |

The output conforms to the challenge submission format.

---

# Future Improvements

- Dynamic Job Description parsing
- Multi-JD support
- Incremental embedding updates
- Hybrid retrieval (Dense + BM25)
- LLM-assisted reasoning generation

---

# Author

**Kashyap Kompella**
