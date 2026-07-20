from sentence_transformers import SentenceTransformer

# Load the model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embedding(text: str) -> list[float]:
    """
    Generate embedding for a single text chunk.
    """

    embedding = model.encode(text)

    return embedding.tolist()