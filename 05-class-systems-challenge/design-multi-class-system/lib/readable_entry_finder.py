class ReadableEntryFinder:
    def __init__(self, diary):
        self.diary = diary

    def best_entry_for_time_available(self, time_available, wpm):
        if len(self.diary.entry_list) == 0:
            return "You haven't made any entries yet!"
        words_to_read = time_available * wpm
        entry_lengths = [entry.word_count() for entry in self.diary.entry_list]
        difference_to_target = [(words_to_read - entry_length) for entry_length in entry_lengths]
        diff_entry_dict = dict(zip(self.diary.entry_list, difference_to_target))
        none_negative_entries = dict(filter(lambda item: item[1] >= 0, diff_entry_dict.items()))
        if len(none_negative_entries) == 0:
            return ("No entries for the time you have available!")
        sorted_entries = sorted(none_negative_entries.items(), key=lambda x: x[1])
        return sorted_entries[0][0].formatted()