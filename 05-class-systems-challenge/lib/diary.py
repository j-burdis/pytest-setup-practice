from math import ceil

class Diary:
    def __init__(self):
        self._diary_entries = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self._diary_entries.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self._diary_entries

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        word_counts = [entry.count_words() for entry in self._diary_entries]
        return sum(word_counts)
        # or ...
        # total = 0
        # for entry in self._diary_entries:
        #     total += entry.count_words()
        # return total
        

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        if wpm == 0:
            raise Exception("Can't calculate a reading time for 0 wpm")
        elif len(self._diary_entries) == 0:
            raise Exception("No diary entries yet")
        return ceil(self.count_words()/wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        if len(self._diary_entries) == 0:
            return None
        
        words_to_read = wpm * minutes
        
        # create list of lengths of each entry in same order
        entry_lengths = [len(entry._contents.split()) for entry in self._diary_entries]
        
        # create list of the difference between entry length and words_to_read
        difference_to_target = [(words_to_read - entry_length) for entry_length in entry_lengths]
        
        # zip entry instance to difference to target amount
        diff_entry_dict = dict(zip(self._diary_entries, difference_to_target))
        
        # remove negative values, which are longer than target words_to_read
        none_negative_entries = dict(filter(lambda item: item[1] >= 0, diff_entry_dict.items()))
        
        # prevent errors from empty dictionaries
        if len(none_negative_entries) == 0:
            return None

        # sort the remaining entries with the lowest first (closest to target)
        sorted_entries = sorted(none_negative_entries.items(), key=lambda x: x[1])
        
        # return list of tuples, from which we take the first element of the first tuple
        # when there are two entries of the same length then first is returned
        return sorted_entries[0][0]
