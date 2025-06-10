import pytest
from lib.diary import Diary
from lib.secret_diary import SecretDiary

def test_locked_diary_cannot_be_read():
    diary = Diary("my contents")
    sdiary = SecretDiary(diary)
    with pytest.raises(Exception) as e:
        sdiary.read()
    assert str(e.value) == "Go away!"

def test_diary_can_be_read_when_unlocked():
    diary = Diary("my contents")
    sdiary = SecretDiary(diary)
    sdiary.unlock()
    assert sdiary.read() == "my contents"

def test_diary_cannot_be_read_after_locking():
    diary = Diary("my contents")
    sdiary = SecretDiary(diary)
    sdiary.unlock()
    sdiary.lock()
    with pytest.raises(Exception) as e:
        sdiary.read()
    assert str(e.value) == "Go away!"