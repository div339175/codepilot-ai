from pathlib import Path

from app.core.parser import parse_repository

files = parse_repository(Path("repos/langgraph"))

print(files[0].name)
print(files[0].language)
print(files[0].path)
print(files[0].size)