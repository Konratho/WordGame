


def readFile(path: str) -> list:
    file = open(path)
    words = file.readlines() # This returns the line-contents of the .txt as a list of strings
    file.close()
    return words