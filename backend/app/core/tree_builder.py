from pathlib import Path

from app.schemas.repository_tree import RepositoryTreeNode


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
}


def build_tree(path: Path, root: Path) -> RepositoryTreeNode:

    if path.is_file():

        return RepositoryTreeNode(
            name=path.name,
            path=str(path.relative_to(root)),
            type="file",
        )

    node = RepositoryTreeNode(
        name=path.name,
        path=str(path.relative_to(root)) if path != root else "",
        type="folder",
    )

    for child in sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower())):

        if child.name in IGNORE_DIRS:
            continue

        node.children.append(build_tree(child, root))

    return node