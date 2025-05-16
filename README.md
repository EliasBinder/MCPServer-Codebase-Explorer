# MCP Server: Codebase Explorer

## Description
Allows a LLM to explore a codebase and answer questions about it. It can explore the folder structure while taking into account `.agentignore` files. It can also read from files, however, it cannot modify the codebase. This server provides a read-only interface to the codebase.

## Functionality

- Explore the folder structure
  - `list_files_in_directory(path)`: Lists all files and directories in the given path. This includes hidden files and works non-recursively.
  - `list_files_in_root_directory()`: Lists all files and directories in the root directory. This includes hidden files and works non-recursively. It is a wrapper around `list_files_in_directory("/")` to make it easier to call.
- Explore files
  - `get_file_content(path)`: Reads the content of a file. Consider using `get_outline_from_file(path, regex)` to get an overview of the file and query it for specific information.
  - `get_specific_file_content(path, regex)`: If the file is a source-code file, it will query the file for the given regex. The LLM can suggest a regex, e.g. to list all functions or classes in the file. This is useful to get an overview of the file without reading the entire content. The regex should be a string, e.g. `"def\s+\w+\s*\(.*\):"` to match all function definitions in Python files.
  - `find_files_with_content(regex_or_str)`: Lists all file paths in the codebase where their content contain the given regex or string. The content should be a string or a regex, e.g. "translation|i18n" to match all occurencies of the string "translation" or "i18n" in the codebase.
