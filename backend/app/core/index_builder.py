from pathlib import Path
import traceback

from app.core.parser import parse_repository
from app.core.chunker import chunk_text
from app.core.embeddings import generate_embedding
from app.core.vector_store import VectorStore

BATCH_SIZE = 256

def build_index(repo_path: Path):

    try:
        repository = repo_path.name

        print(f"Starting index build for: {repository}")

        store = VectorStore()

        files = parse_repository(repo_path)

        print(f"Found {len(files)} files")

        all_chunks = []
        all_metadata = []

        for i, file in enumerate(files, start=1):

            print(f"[{i}/{len(files)}] Processing {file.path}")

            chunks = chunk_text(file.content)
            
            if not chunks:
                continue

            for chunk in chunks:

                all_chunks.append(chunk)

                all_metadata.append(
                    {
                        "repository": repository,
                        "file": file.path,
                        "language": file.language,
                        "chunk": chunk,
                    }
                )
        print(f"Generated {len(all_chunks)} chunks")
        
        # Generate embeddings in batches
        for i in range(0, len(all_chunks), BATCH_SIZE):

            batch_chunks = all_chunks[i:i + BATCH_SIZE]
            batch_metadata = all_metadata[i:i + BATCH_SIZE]

            print(
                f"Embedding batch {i // BATCH_SIZE + 1} "
                f"({len(batch_chunks)} chunks)"
            )

            embeddings = generate_embedding(batch_chunks)

            for embedding, metadata in zip(embeddings, batch_metadata):

                store.add(
                    embedding,
                    metadata
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