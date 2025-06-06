from math import ceil

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self._title = title
        self._contents = contents
        self._read_so_far = 0


    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        word_count = len(self._contents.split())
        return word_count


    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        if wpm == 0:
            raise Exception("Can't calculate a reading time for 0 wpm")
        return ceil(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        words_to_read = round(wpm * minutes)
        all_words = self._contents.split()
        if self._read_so_far >= len(all_words):
            self._read_so_far = 0
        
        chunk_start = self._read_so_far
        chunk_end = self._read_so_far + words_to_read
        chunk_words = all_words[chunk_start:chunk_end]
        self._read_so_far = chunk_end
        return " ".join(chunk_words)
