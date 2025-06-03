from lib.make_snippet import *

def test_string_is_the_argument():
    result = make_snippet("snip")
    assert type(result) == str

def test_string_returned_if_five_or_less_words():
    result = make_snippet("The quick brown fox jumped")
    assert result == "The quick brown fox jumped"

def test_snippet_is_more_than_five_words():
    result = make_snippet("The quick brown fox jumped over")
    result_length = len(result.split())
    assert result_length == 5

def test_snipped_string_ends_in_dots():
    result = make_snippet("The quick brown fox jumped over")
    assert result[-3:] == "..."
