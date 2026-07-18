from pathlib import Path
from app.core.index_builder import build_embeddings

docs = build_embeddings(Path("repos/langgraph"))

print(len(docs))
print(docs[0]["file"])
print(len(docs[0]["embedding"]))