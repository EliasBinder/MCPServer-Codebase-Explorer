import re

from gitignore_parser import Path

from utils.agentignore_parser import is_path_ignored

def list_files_with_matching_regex(base_path: str, regex: str):
    base = Path(base_path).resolve()
    matching_files = []
    pattern = re.compile(regex)
    for file_path in base.rglob("*"):
        combined_path = file_path.resolve()
        if file_path.is_file() and not is_path_ignored(combined_path):
            try:
                with file_path.open("r", encoding="utf-8") as f:
                    content = f.read()
                    if pattern.search(content):
                        matching_files.append(str(file_path))
            except (UnicodeDecodeError, OSError):
                # Skip binary or unreadable files
                continue

    return matching_files
