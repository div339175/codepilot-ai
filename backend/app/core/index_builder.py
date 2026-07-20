from pathlib import Path
import traceback

from app.core.parser import parse_repository
from app.core.chunker import chunk_text
from app.core.embeddings import generate_embedding
from app.core.vector_store import VectorStore


def build_index(repo_path: Path):

    try:
        repository = repo_path.name

        print(f"Starting index build for: {repository}")

        store = VectorStore()

        files = parse_repository(repo_path)

        print(f"Found {len(files)} files")

        for i, file in enumerate(files, start=1):

            print(f"[{i}/{len(files)}] Processing {file.path}")

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

        print("Saving FAISS index...")

        store.save(repository)

        print("Index build completed successfully.")

        return store

    except Exception as e:

        print("=" * 60)
        print("INDEX BUILD FAILED")
        print("=" * 60)
        print(f"Repository: {repo_path}")
        print(f"Error: {e}")
        traceback.print_exc()
        print("=" * 60)

        raise