import pytest
from lib.diary import Diary

# Initially there are no entries
def test_diary_starts_with_no_entries():
    diary = Diary()
    assert diary.all() == []

def test_starts_with_word_count_zero():
    diary = Diary()
    assert diary.count_words() == 0

def test_initially_reading_time_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.reading_time(2)
    message = str(e.value)
    assert message == "No diary entries yet"
