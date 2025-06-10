from lib.diary import Diary

def test_diary_initialised_with_a_contents_string():
    entry = Diary("first entry")
    assert entry._contents == "first entry"

def test_read_method_returns_contents():
    entry = Diary("first entry")
    assert entry.read() == "first entry"