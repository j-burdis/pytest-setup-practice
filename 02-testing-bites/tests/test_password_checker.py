import pytest
from lib.password_checker import *

def test_checks_long_password_is_correct():
    password = PasswordChecker()
    assert password.check("12345678") == True

def test_checks_short_password_raises_exception():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("1234567")
    error = str(e.value)
    assert error == "Invalid password, must be 8+ characters."
