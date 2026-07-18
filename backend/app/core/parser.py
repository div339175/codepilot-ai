from pathlib import Path
from app.core.file_reader import read_file

# Phase 1 — Scanner

IGNORE_DIRS = {
    ".git",
    ".github",
    "__pycache__",
    "venv",
    ".venv",
    "node_modules",
    "dist",
    "build",
    ".idea",
    ".vscode",
    ".pytest_cache",
    ".mypy_cache",
}
SUPPORTED_EXTENSIONS = {
    ".py",
    ".cpp",
    ".c",
    ".h",
    ".hpp",
    ".java",
    ".js",
    ".ts",
    ".tsx",
    ".go",
    ".rs",
    ".md",
    ".json",
    ".yaml",
    ".yml",
    ".html",
    ".css",
    ".sql",
    ".xml",
    ".toml",
    ".ini",
    ".txt",
    ".sh"
}

SPECIAL_FILES = {
    "Dockerfile",
    "Makefile",
    "LICENSE",
    ".gitignore"
}
def is_supported_file(file: Path) -> bool:
    """
    Returns True if the file should be parsed.
    """

    if file.name in SPECIAL_FILES:
        return True

    return file.suffix.lower() in SUPPORTED_EXTENSIONS


def scan_repository(repo_path: Path):

    files = []

    for path in repo_path.rglob("*"):

        if path.is_dir():
            continue

        if any(part in IGNORE_DIRS for part in path.parts):
            continue

        if not is_supported_file(path):
            continue

        files.append(path)

    return files

# Phase 2 — Metadata

LANGUAGE_MAP = {

     ".py": "python",
    ".cpp": "cpp",
    ".c": "c",
    ".h": "c",
    ".hpp": "cpp",
    ".java": "java",
    ".js": "javascript",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".go": "go",
    ".rs": "rust",
    ".html": "html",
    ".css": "css",
    ".sql": "sql",
    ".json": "json",
    ".yaml": "yaml",
    ".yml": "yaml",
    ".md": "markdown",
    ".txt": "text",
    ".xml": "xml",
    ".toml": "toml",
    ".ini": "ini",
    ".sh": "shell"
}


def file_metadata(file: Path,repo_path: Path):

    extension = file.suffix.lower()

    return {

    "name": file.name,

    "path": str(file.relative_to(repo_path)),

    "extension": extension,

    "language": LANGUAGE_MAP.get(extension, "unknown"),

    "size": file.stat().st_size,

    "content": read_file(file)
}

# Phase 3

def parse_repository(repo_path: Path):

    files = scan_repository(repo_path)

    metadata = []

    for file in files:

        metadata.append(file_metadata(file,repo_path))

    return metadata

