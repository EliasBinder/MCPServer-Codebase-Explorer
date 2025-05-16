import os
from gitignore_parser import parse_gitignore

agentignore_matcher = None

def load_agentignore_file(base_path):
    """
    Load the agentignore file and return a list of patterns.
    """

    agentignore_path = os.path.join(base_path, ".agentignore")
    if not os.path.exists(agentignore_path):
        return False  # Changed from True to False

    global agentignore_matcher  # Added this line to use the global variables

    agentignore_matcher = parse_gitignore(agentignore_path)


def is_path_ignored(path):
    """
    Check if the given path is ignored by the agentignore file.
    """
    if agentignore_matcher is None:
        return False

    return agentignore_matcher(path)
