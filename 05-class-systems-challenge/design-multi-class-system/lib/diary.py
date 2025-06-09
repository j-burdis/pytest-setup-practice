import re

class Diary:
    def __init__(self):
        self.entry_list = []

    def add(self, entry):
        self.entry_list.append(entry)

    def all_entries(self):
        if self.entry_list:
            return [entry.formatted() for entry in self.entry_list]
        else:
            return "You haven't made any entries yet!"

    def best_entry_for_time_available(self, time_available, wpm):
        if len(self.entry_list) == 0:
            return "You haven't made any entries yet!"
        words_to_read = time_available * wpm
        entry_lengths = [entry.word_count() for entry in self.entry_list]
        difference_to_target = [(words_to_read - entry_length) for entry_length in entry_lengths]
        diff_entry_dict = dict(zip(self.entry_list, difference_to_target))
        none_negative_entries = dict(filter(lambda item: item[1] >= 0, diff_entry_dict.items()))
        if len(none_negative_entries) == 0:
            return ("No entries for the time you have available!")
        sorted_entries = sorted(none_negative_entries.items(), key=lambda x: x[1])
        return sorted_entries[0][0].formatted()

    def find_mobile_numbers(self):
        number_list = []
        for entry in self.all_entries():
            number_search = re.findall(r'\b0\d{10}\b', entry)
            if number_search:
                number_list.append(number_search[0])
        return number_list

