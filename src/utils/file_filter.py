IGNORE_EXTENSIONS = [
    ".lock",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".ico"
]

IGNORE_FILES = [
    "package-lock.json",
    "yarn.lock"
]

def should_review_file(filename):

    for ext in IGNORE_EXTENSIONS:

        if filename.endswith(ext):
            return False

    for ignored in IGNORE_FILES:

        if ignored in filename:
            return False

    return True