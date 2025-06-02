from lib.check_codeword import *

def test_check_codeword_return_correct():
        result = check_codeword("horse")
        assert result == "Correct! Come in."

def test_check_codeword_return_close():
        result = check_codeword("hose")
        assert result == "Close, but nope."

def test_correct_first_letter_wrong_last_letter():
        result = check_codeword("horses")
        assert result == "WRONG!"

def test_correct_last_letter_wrong_first_letter():
        result = check_codeword("mouse")
        assert result == "WRONG!"
