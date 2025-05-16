from utils.scan_directory import list_directory


if __name__ == "__main__":
  codebase_root = "/Users/eliasbinder/Documents/Coontent"
  relative_path = "/microservice_scheduler"
  print(list_directory(codebase_root, relative_path))
