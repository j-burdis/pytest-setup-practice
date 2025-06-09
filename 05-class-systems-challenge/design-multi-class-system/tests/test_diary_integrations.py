from lib.diary import Diary
from lib.diary_entry import DiaryEntry

def test_add_entry_appends_to_entry_list():
    diary = Diary()
    entry1 = DiaryEntry("First", "My first entry")
    diary.add(entry1)
    assert diary.entry_list == [entry1]

def test_add_entry_appends_to_multiple_entries_list():
    diary = Diary()
    entry1 = DiaryEntry("First", "My first entry")
    entry2 = DiaryEntry("Second", "My second entry")
    entry3 = DiaryEntry("Third", "My third entry")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.entry_list == [entry1, entry2, entry3]

def test_all_entries_returns_list_of_entries():
    diary = Diary()
    entry1 = DiaryEntry("First", "My first entry")
    entry2 = DiaryEntry("Second", "My second entry")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.all_entries() == ["First: My first entry", "Second: My second entry"]

def test_show_entries_for_time_available():
    diary = Diary()
    entry1 = DiaryEntry("First", "First entry")
    entry2 = DiaryEntry("Second", "My second entry")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.best_entry_for_time_available(2, 1) == "First: First entry"

def test_returns_one_out_of_two_mobile_numbers():
    diary = Diary()
    entry1 = DiaryEntry("First", "a failing number 0074324532443243")
    entry2 = DiaryEntry("Second", "a passing number 07123456789")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.find_mobile_numbers() == ["07123456789"]

def test_returns_two_out_of_three_mobile_numbers():
    diary = Diary()
    entry1 = DiaryEntry("First", "a failing number 0074324532443243")
    entry2 = DiaryEntry("Second", "a passing number 07123456789")
    entry3 = DiaryEntry("Third", "another passing number 07987654321")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.find_mobile_numbers() == ["07123456789", "07987654321"]
