import re

class PhoneNumberFinder:
    def __init__(self, diary):
        self.diary = diary
    
    def find_mobile_numbers(self):
        number_list = []
        for entry in self.diary.all_entries():
            number_search = re.findall(r'\b0\d{10}\b', entry)
            if number_search:
                number_list.append(number_search[0])
        return number_list