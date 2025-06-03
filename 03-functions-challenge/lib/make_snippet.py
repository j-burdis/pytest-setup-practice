def make_snippet(string):
    word_list = string.split()
    if len(word_list) >  5:
        snip = " ".join(word_list[:5])
        return snip + "..."
    else:
        return string
