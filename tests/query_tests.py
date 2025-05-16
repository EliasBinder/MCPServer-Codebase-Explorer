from utils.agentignore_parser import load_agentignore_file
from utils.query import list_files_with_matching_regex
if __name__ == "__main__":
  codebase_root = "/Users/eliasbinder/Documents/KeepInMind/vog/app"
  regex = "cooperatives"
  load_agentignore_file(codebase_root)
  print(list_files_with_matching_regex(codebase_root, regex))
