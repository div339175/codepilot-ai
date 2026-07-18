import numpy as np

from app.core.embeddings import generate_embedding
from app.core.vector_store import VectorStore


def semantic_search(
    repository: str,
    query: str,
    top_k: int = 5
):

    store = VectorStore()

    # Load the FAISS index for the specified repository
    store.load(repository)

    query_embedding = generate_embedding(query)

    query_vector = np.array(
        [query_embedding],
        dtype="float32"
    )

    distances, indices = store.index.search(
        query_vector,
        top_k
    )

    results = []

    for distance, index in zip(distances[0], indices[0]):

        if index == -1:
            continue

        metadata = store.metadata[index]

        results.append(
            {
                "repository": metadata["repository"],
                "score": float(distance),
                "file": metadata["file"],
                "language": metadata["language"],
                "chunk": metadata["chunk"]
            }
        )

    return results