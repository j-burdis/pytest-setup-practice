import pytest
from lib.diary import Diary
from lib.diary_entry import DiaryEntry

def test_adds_two_entries_then_lists_them():
    diary = Diary()
    entry1 = DiaryEntry("Title 1", "Contents 1")
    entry2 = DiaryEntry("Title 2", "Contents 2")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.all() == [entry1, entry2]

def test_counts_words_in_all_diary_entries():
    diary = Diary()
    entry1 = DiaryEntry("Title 1", "Contents 1")
    entry2 = DiaryEntry("Title 2", "Contents 2")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.count_words() == 4

def test_return_total_reading_time_for_all_entries():
    diary = Diary()
    entry1 = DiaryEntry("Title 1", "Contents 1")
    entry2 = DiaryEntry("Title 2", "Contents 2 3")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.reading_time(2) == 3

def test_wpm_zero_reading_time_for_all_entries():
    diary = Diary()
    entry1 = DiaryEntry("Title 1", "Contents 1")
    entry2 = DiaryEntry("Title 2", "Contents 2")
    diary.add(entry1)
    diary.add(entry2)
    with pytest.raises(Exception) as e:
        diary.reading_time(0)
    assert str(e.value) == "Can't calculate a reading time for 0 wpm"

# tests all scenarios (I think)
def test_returns_best_entry_for_reading_time_with_multiple_entries():
    diary = Diary()
    entry3 = DiaryEntry("Title 3", "shortest contents")
    entry1 = DiaryEntry("Title 1", "shorter contents example")
    entry4 = DiaryEntry("Title 4", "shorter contents example")
    entry2 = DiaryEntry("Title 2", "this is a longer contents example")
    diary.add(entry3)
    diary.add(entry1)    
    diary.add(entry4)    
    diary.add(entry2)
    assert diary.find_best_entry_for_reading_time(1, 3) == entry1

def test_returns_none_if_there_are_no_diary_entries():
    diary = Diary()
    assert diary.find_best_entry_for_reading_time(1, 3) == None

def test_returns_none_if_only_longer_entries():
    diary = Diary()
    entry2 = DiaryEntry("Title 2", "this is a longer contents example")
    diary.add(entry2)
    assert diary.find_best_entry_for_reading_time(1, 3) == None
