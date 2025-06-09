from lib.diary import Diary

def test_initially_diary_is_empty_list():
    diary = Diary()
    assert diary.entry_list== []

def test_all_entries_returns_message_when_empty():
    diary= Diary()
    assert diary.all_entries() == "You haven't made any entries yet!"