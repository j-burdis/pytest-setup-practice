def reading_time_in_minutes(text):
    if isinstance(text, type(None)):
        raise Exception("Enter a string input")
    word_count = len(text.split())
    time_in_minutes = word_count / 200
    return round(time_in_minutes)
