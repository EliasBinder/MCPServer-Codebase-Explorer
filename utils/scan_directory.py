import os
import json

from utils.agentignore_parser import is_path_ignored

def list_directory(base_path, path):
  try:
    # Remove starting slash from path if it exists
    if path.startswith("/"):
      path = path[1:]

    # List all files and directories in the given path
    combined_path = os.path.join(base_path, path)
    items = os.listdir(combined_path)

    # Create a list to hold the results
    results = []

    for item in items:
      item_path = "/" + os.path.join(path, item)
      if (is_path_ignored(os.path.join(combined_path, item))):
        continue  # Skip ignored paths
      if os.path.isdir(os.path.join(combined_path, item)):
        results.append({"type": "directory", "path": item_path, "name": item})
      else:
        results.append({"type": "file", "path": item_path, "name": item})

    # Return the results as a JSON string
    return json.dumps(results, indent=2)
  except Exception as e:
    # Handle any exceptions that occur
    return json.dumps({"error": str(e)}, indent=2)
