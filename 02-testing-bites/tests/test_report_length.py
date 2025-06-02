from lib.report_length import *

def test_correct_string_length():
    result = report_length("Hello")
    assert result == "This string was 5 characters long."