from lib.diary_entry import DiaryEntry

def test_diary_entry_created_with_title_and_contents():
    entry = DiaryEntry("Day one", "My first day")
    assert entry.title == "Day one"
    assert entry.contents == "My first day"

def test_word_count_returns_contents_length():
    entry = DiaryEntry("Day one", "My first day")
    assert entry.word_count() == 3

def test_entry_formatted_correctly():
    entry = DiaryEntry("Day one", "My first day")
    assert entry.formatted() == "Day one: My first day"