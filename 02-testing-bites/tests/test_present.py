import pytest
from lib.present import * 

def test_contents_are_unwrapped_after_wrapping():
    present = Present()
    present.wrap("phone")
    assert present.unwrap() == "phone"

def test_raises_error_when_present_is_already_wrapped():
    present = Present()
    present.wrap("watch")
    with pytest.raises(Exception) as e:
        present.wrap("phone")
    err_message = str(e.value)
    assert err_message == "A contents has already been wrapped."

def test_raises_error_when_present_is_unwrapped():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    e_message = str(e.value)
    assert e_message == "No contents have been wrapped."

def test_wrapping_already_wrapped_preserves_value():
    present = Present()
    present.wrap("phone")
    with pytest.raises(Exception) as e:
        present.wrap("watch")
    assert present.unwrap() == "phone"