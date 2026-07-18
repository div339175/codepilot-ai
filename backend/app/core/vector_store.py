from pathlib import Path
import faiss
import numpy as np
import pickle


class VectorStore:

    def __init__(self):

        self.dimension = 384
        self.index = faiss.IndexFlatL2(self.dimension)
        self.metadata = []

    def add(self, embedding, metadata):

        vector = np.array([embedding], dtype="float32")

        self.index.add(vector)

        self.metadata.append(metadata)

    def save(self, repository):

        folder = Path("indexes") / repository

        folder.mkdir(parents=True, exist_ok=True)

        faiss.write_index(
            self.index,
            str(folder / "code.index")
        )

        with open(folder / "metadata.pkl", "wb") as f:
            pickle.dump(self.metadata, f)

    def load(self, repository):

        folder = Path("indexes") / repository

        self.index = faiss.read_index(
            str(folder / "code.index")
        )

        with open(folder / "metadata.pkl", "rb") as f:
            self.metadata = pickle.load(f)