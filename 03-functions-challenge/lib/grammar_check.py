def grammar_checker(text):
    if isinstance(text, type(None)) or len(text) == 0:
        raise Exception("Enter a sentence to check.")
    elif text[0] != text[0].upper() and text[-1] not in [".", "?", "!"]:
        return "Check your capital letters and punctuation."
    elif text[0] != text[0].upper():
        return "Check your capital letters."
    elif text[-1] not in ".?!":
        return "Check your sentence ending."
    else:
        return "Good job!"
