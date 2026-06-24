import numpy as np
from src.parser.jd_loader import load_jd
from src.features.embedding_generator import generate_embedding

def generate_jd_embedding():
    jd_text=load_jd("data/raw/jd.txt")
    jd_embedding=generate_embedding(jd_text)
    return jd_embedding
