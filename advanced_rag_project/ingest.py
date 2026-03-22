import os
import numpy as np
import endee

from embedder import get_embedding

texts = []

for file in os.listdir("data"):
    with open(f"data/{file}", "r", encoding="utf-8") as f:
        texts += f.readlines()

embeddings = get_embedding(texts)

np.save("vectors.npy", embeddings)
np.save("texts.npy", texts)

print("Vectors stored using Endee environment")