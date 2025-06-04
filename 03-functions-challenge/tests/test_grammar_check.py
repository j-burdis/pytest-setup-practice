import pytest
from lib.grammar_check import *

def test_empty_string_returns_error():
    with pytest.raises(Exception) as e:
        grammar_checker("")
    message = str(e.value)
    assert message == "Enter a sentence to check."

def test_checks_good_grammar():
    result = grammar_checker("A good sentence.")
    assert result == "Good job!"

def test_checks_capitalisation_at_start():
    result = grammar_checker("a less good sentence.")
    assert result == "Check your capital letters."

def test_checks_punctuation_at_end():
    result = grammar_checker("Also a bad sentence")
    assert result == "Check your sentence ending."

def test_check_capitalisation_and_punctuation():
    result = grammar_checker("the worse sentence")
    assert result == "Check your capital letters and punctuation."

def test_check_none_values():
    with pytest.raises(Exception) as e:
        result = grammar_checker(None)
    message = str(e.value)
    assert message == "Enter a sentence to check."
