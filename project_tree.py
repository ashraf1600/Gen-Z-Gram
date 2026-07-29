from pathlib import Path

IGNORE = {
    "node_modules",
    "__pycache__",
    ".git",
    ".vscode",
    "env",
    "venv",
    "dist",
    "build",
    "migrations",
}

def tree(path, prefix=""):
    entries = [
        p for p in sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
        if p.name not in IGNORE
    ]

    for i, entry in enumerate(entries):
        connector = "└── " if i == len(entries) - 1 else "├── "
        print(prefix + connector + entry.name)

        if entry.is_dir():
            extension = "    " if i == len(entries) - 1 else "│   "
            tree(entry, prefix + extension)

tree(Path("."))