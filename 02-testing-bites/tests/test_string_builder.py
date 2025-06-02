from lib.string_builder import StringBuilder

def test_initially_returns_empty_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

def test_initial_string_length_is_zero():
    string_builder = StringBuilder()
    assert string_builder.size() == 0

def test_adding_multiple_strings_joins_them():
    string_builder = StringBuilder()
    string_builder.add("hey")
    string_builder.add(" ")
    string_builder.add("everyone")
    assert string_builder.output() == "hey everyone"

def test_adding_multiple_strings_has_total_size():
    string_builder = StringBuilder()
    string_builder.add("hey")
    string_builder.add(" ")
    string_builder.add("everyone")
    assert string_builder.size() == 12
