from pathlib import Path

from app.core.parser import parse_repository
from app.core.chunker import chunk_text
from app.core.embeddings import generate_embedding
from app.core.vector_store import VectorStore


def build_index(repo_path: Path):

    repository = repo_path.name

    store = VectorStore()

    files = parse_repository(repo_path)

    for file in files:

        chunks = chunk_text(file.content)

        for chunk in chunks:

            embedding = generate_embedding(chunk)

            store.add(
                embedding,
                {
                    "repository": repository,
                    "file": file.path,
                    "language": file.language,
                    "chunk": chunk
                }
            )

    # Save inside indexes/<repository>/
    store.save(repository)

    return store