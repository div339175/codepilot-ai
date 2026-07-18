from pathlib import Path

from app.core.parser import parse_repository
from app.core.chunker import chunk_text
from app.core.embeddings import generate_embedding


def build_embeddings(repo_path: Path):

    files = parse_repository(repo_path)

    documents = []

    for file in files:

        chunks = chunk_text(file["content"])

        for chunk in chunks:

            documents.append({

                "file": file["path"],

                "language": file["language"],

                "chunk": chunk,

                "embedding": generate_embedding(chunk)

            })

    return documents