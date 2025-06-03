def count_words(string):
    if not isinstance(string, str):
        raise Exception("Enter a string input")
    return len(string.split())
