import os
import json
import subprocess

def list_files_with_matching_regex(base_path: str, regex: str):
  # List all files in the given path that match the regex
  # Use grep command to list relative file paths with matching content
  # Check if the directory is a git repository
  is_git_repo = False
  try:
    # Run git rev-parse to check if we're in a git repo
    result = subprocess.run(
      ['git', 'rev-parse', '--is-inside-work-tree'],
      cwd=base_path,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE,
      text=True,
      check=False
    )
    is_git_repo = result.returncode == 0 and result.stdout.strip() == 'true'
  except (subprocess.SubprocessError, FileNotFoundError):
    is_git_repo = False

  # Command to run depends on whether it's a git repo
  if is_git_repo:
    # Use git ls-files to respect .gitignore
    command = f"cd {base_path} && git ls-files | xargs grep -l '{regex}'"
  else:
    # Use regular grep as before
    command = f"grep -rl '{regex}' {base_path}"

  # Execute the command
  process = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

  if process.returncode != 0 and process.returncode != 1:  # grep returns 1 if no matches found
    return json.dumps({"error": f"Command failed with error: {process.stderr}"}, indent=2)

  # Split the result into a list of file paths
  file_paths = process.stdout.splitlines()

  # Create a list to hold the results
  results = []

  for path in file_paths:
    # For git repos, paths are already relative to the repo root
    # For non-git repos, we need to make them relative to base_path
    if is_git_repo:
      # Ensure full path for consistency
      full_path = os.path.join(base_path, path)
      relative_path = path
    else:
      full_path = path
      relative_path = os.path.relpath(path, base_path)

    # Only include the file if it exists (sanity check)
    if os.path.exists(full_path):
      results.append({"path": relative_path})

  # Return the results as a JSON string
  return json.dumps(results, indent=2)
