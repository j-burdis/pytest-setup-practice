import pytest
from lib.diary_entry import DiaryEntry

def test_errors_on_empty_title_and_contents():
    with pytest.raises(Exception) as e:
        DiaryEntry("", "")
    assert str(e.value) == "Diary entries must have a title and contents"

def test_title_and_contents_have_correct_format():
    entry = DiaryEntry("My Title", "These are the contents")
    result = entry.format()
    assert result == "My Title: These are the contents"

def test_checks_word_count():
    entry = DiaryEntry("My Title", "These are the contents")
    result = entry.count_words()
    assert result == 4

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
    result = entry.reading_chunk(4, 3)
    assert result ==  "These are the contents These are the contents These are the contents"

def test_reading_chunk_two_wpm_one_minute_called_twice():
    entry = DiaryEntry("My Title", "These are the contents These are the contents These are the contents")
    assert entry.reading_chunk(2,1) == "These are"
    assert entry.reading_chunk(2,1) == "the contents"

def test_reading_chunk_two_wpm_one_minute_called_many_times():
    entry = DiaryEntry("My Title", "These are the contents These are the contents These are the contents")
    assert entry.reading_chunk(2,1) == "These are"
    assert entry.reading_chunk(2,1) == "the contents"
    assert entry.reading_chunk(1,1) == "These"

def test_reading_chunk_wraps_around_on_mulitple_calls():
    entry = DiaryEntry("My Title", "These are the contents These are the contents These are the contents")
    assert entry.reading_chunk(6,1) == "These are the contents These are"
    assert entry.reading_chunk(4,1) == "the contents These are"
    assert entry.reading_chunk(3,1) == "the contents"
    assert entry.reading_chunk(4,1) == "These are the contents"