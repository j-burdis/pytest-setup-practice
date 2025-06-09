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
