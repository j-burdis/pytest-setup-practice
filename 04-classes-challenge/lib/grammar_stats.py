class GrammarStats:
    def __init__(self):
        self.checks_record = [0, 0]

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if len(text) == 0:
            self.checks_record[1] += 1
            return False
        if text[0] == text[0].upper() and text[-1] in [".", "?", "!"]:
            self.checks_record[0] += 1
            self.checks_record[1] += 1
            return True
        else:
            self.checks_record[1] += 1
            return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if self.checks_record[0] == 0 or sum(self.checks_record) == 0:
            return 0
        percentage_check = round((self.checks_record[0]/self.checks_record[1]) * 100)
        return int(percentage_check)
