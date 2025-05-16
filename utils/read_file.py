import json
import re
import os

def read_file_contents(base_path: str, path: str, regex: str | None = None):
  # Remove starting slash from path if it exists
  if path.startswith("/"):
    path = path[1:]

  # List all files and directories in the given path
  combined_path = os.path.join(base_path, path)
  try:
    # Open the file in read mode
    with open(combined_path, 'r') as file:
      # Read the contents of the file
      contents = file.read()

      if regex is None:
        # If no regex is provided, return the contents of the file
        return contents

      # Return all regex matches in the file
      matches = re.findall(regex, contents)
      if matches:
        # If there are matches, return them as a JSON string
        return json.dumps(matches, indent=2)
      else:
        # If no matches are found, return an empty list
        return json.dumps({"error": "No matches for given Regex found. Please try another one."}, indent=2)

  except FileNotFoundError:
    # Handle the case where the file does not exist
    return json.dumps({"error": "File Not Found. Please check if the path is correct"}, indent=2)
