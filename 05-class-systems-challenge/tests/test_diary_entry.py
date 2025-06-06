import pytest
from lib.diary_entry import DiaryEntry

# When we create a new entry
# We can display it's title and contents

def test_create_diary_entry_and_get_title_contents():
    entry = DiaryEntry("title 1", "contents 1")
    assert entry._title == "title 1"
    assert entry._contents == "contents 1"

def test_count_words_returns_correct_value():
    entry = DiaryEntry("title 1", "contents 1")
    assert entry.count_words() == 2

def test_checks_reading_time():
    entry = DiaryEntry("My Title", "These are the contents These are the contents These are the contents")
    result = entry.reading_time(4)
    assert result == 3

def test_checks_reading_time_with_wpm_zero():
    entry = DiaryEntry("My Title", "These are the contents These are the contents These are the contents")
    with pytest.raises(Exception) as e:
        entry.reading_time(0)
    assert str(e.value) == "Can't calculate a reading time for 0 wpm"

def test_checks_reading_chunk_returns_correct_length():
    entry = DiaryEntry("My Title", "These are the contents These are the contents These are the contents")
    result = entry.reading_chunk(4, 2)
    assert result ==  "These are the contents These are the contents"

def test_reading_chunk_wraps_around_on_mulitple_calls():
    entry = DiaryEntry("My Title", "These are the contents1 These are the contents2 These are the contents3")
    assert entry.reading_chunk(6,1) == "These are the contents1 These are"
    assert entry.reading_chunk(4,1) == "the contents2 These are"
    assert entry.reading_chunk(3,1) == "the contents3"
    assert entry.reading_chunk(4,1) == "These are the contents1"