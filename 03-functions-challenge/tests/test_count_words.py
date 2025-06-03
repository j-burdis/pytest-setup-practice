import pytest
from lib.count_words import *

def test_empty_string_returns_zero():
    result = count_words("")
    assert result == 0

def test_not_empty_string_returns_string_length():
    result = count_words("not an empty string")
    assert result == 4

def test_more_than_one_sentence():
    result = count_words("one sentence. more than one sentence.")
    assert result == 6

def test_input_is_not_a_string():
    with pytest.raises(Exception) as e:
        count_words(1234)
    message = str(e.value)
    assert message == "Enter a string input"
