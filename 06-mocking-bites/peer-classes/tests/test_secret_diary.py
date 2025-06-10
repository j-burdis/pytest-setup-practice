import pytest
from unittest.mock import Mock
from lib.secret_diary import SecretDiary

def test_locked_diary_cannot_be_read():
    diary = Mock()
    sdiary = SecretDiary(diary)
    with pytest.raises(Exception) as e:
        sdiary.read()
    assert str(e.value) == "Go away!"
    diary.read.assert_not_called()

def test_diary_can_be_read_when_unlocked():
    diary = Mock()
    diary.read.return_value = "first entry"
    sdiary = SecretDiary(diary)
    sdiary.unlock()
    assert sdiary.read() == "first entry"
    diary.read.assert_called()

def test_relocked_diary_cannot_be_read():
    diary = Mock()
    sdiary = SecretDiary(diary)
    sdiary.unlock()
    sdiary.lock()
    with pytest.raises(Exception) as e:
        sdiary.read()
    assert str(e.value) == "Go away!"
    diary.read.assert_not_called()

