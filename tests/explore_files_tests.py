from utils.read_file import read_file_contents


if __name__ == "__main__":
  codebase_root = "/Users/eliasbinder/Documents/Coontent"
  relative_path = "/microservice_scheduler/.gitignore"

  print(read_file_contents(codebase_root, relative_path, None))

  # Example regex to match all lines that start with a #
  print("Example regex to match all lines that start with a #")
  # Match all lines that start with a #
  regex_string = "^#.*"
  print(read_file_contents(codebase_root, relative_path, regex_string))
