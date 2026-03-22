from sentence_transformers import SentenceTransformer
from config import MODEL_NAME

model = SentenceTransformer(MODEL_NAME)


def get_embedding(texts):
    return model.encode(texts).tolist()