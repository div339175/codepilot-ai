from sentence_transformers import SentenceTransformer

# Load only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embedding(texts: list[str]) -> list[list[float]]:
    """
    Generate embeddings for multiple text chunks at once.
    """

    embeddings = model.encode(
        texts,
        batch_size=32,
        show_progress_bar=False
    )

    return embeddings.tolist()