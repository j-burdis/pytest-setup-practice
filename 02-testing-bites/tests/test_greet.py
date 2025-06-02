from lib.greet import *

def test_greet_returns_name_param():
    result = greet("Jon")
    assert result == "Hello, Jon!"
