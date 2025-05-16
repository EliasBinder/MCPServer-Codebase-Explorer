from fastmcp import FastMCP
from utils import query, scan_directory
from utils.read_file import read_file_contents
import sys
from utils.agentignore_parser import load_agentignore_file

# Create a server instance
mcp = FastMCP(name="Codebase Explorer")

codebase_root = "/path/to/codebase"  # Replace with the actual path to your codebase

@mcp.tool()
def list_files_in_root_directory():
  """Lists all files and directories in the codebase root directory. This includes hidden files and works non-recursively. It is a wrapper around list_files_in_directory("/") to make it easier to call."""
  return scan_directory.list_directory(codebase_root, "")

@mcp.tool()
def list_files_in_directory(path: str):
  """Lists all files and directories in the given directory. This includes hidden files and works non-recursively."""
  return scan_directory.list_directory(codebase_root, path)

@mcp.tool()
def get_file_content(path: str):
  """Returns the content of a file. Consider using get_outline_from_file(path, regex) to get an overview of the file and query it for specific information."""
  return read_file_contents(codebase_root, path, None)

@mcp.tool()
def get_specific_file_content(path: str, regex: str):
  """Query the file content for the given regex, e.g. to list all functions or classes in the file. All matches of this regex against the file content will be returned. This is useful to get an overview or particular information of the file without reading the entire content. The regex should be a string, e.g. "def\\s+\\w+\\s*\\(.*\\):" to match all function definitions in Python files."""
  return read_file_contents(codebase_root, path, regex)

@mcp.tool()
def find_files_with_content(regex_or_str: str):
  """Lists all file paths in the codebase where their content contain the given regex or string. The content should be a string or a regex, e.g. "translation|i18n" to match all occurencies of the string "translation" or "i18n" in the codebase."""
  return query.list_files_with_matching_regex(codebase_root, regex_or_str)

if __name__ == "__main__":
    # python3 server.py --codebase /path/to/codebase
    codebase_root = sys.argv[2] if len(sys.argv) > 2 else codebase_root
    print(f"Codebase root: {codebase_root}")

    # Load agentignore file
    load_agentignore_file(codebase_root)

    mcp.run()
