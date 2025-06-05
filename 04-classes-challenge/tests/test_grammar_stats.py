from lib.grammar_stats import GrammarStats

# given an empty string is provided
# then return False
def test_return_false_for_an_empty_string():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("") == False

# given a string with correct grammar
# then return True
def test_returns_true_when_there_is_correct_grammar():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Good grammar.")
    assert result == True

# given a string with a lowercase first letter
# then return False
def test_returns_false_for_lowercase_start():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("good grammar.")
    assert result == False

# given a string without punctuation at the end
# then return False
def test_returns_false_for_no_punctuation():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Good grammar")
    assert result == False

# given a string without an uppercase starting letter
# or no punctuation at the end
# then return False
def test_returns_false_for_all_lower_and_no_punctuation():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("good grammar")
    assert result == False

def test_returns_percentage_from_zero_past_checks():
    grammar_stats = GrammarStats()
    result = grammar_stats.percentage_good()
    assert result == 0

def test_percentage_when_all_correct():
    grammar_stats = GrammarStats()
    grammar_stats.check("Good grammar.")
    result = grammar_stats.percentage_good()
    assert result == 100

def test_one_out_of_two_correct():
    grammar_stats = GrammarStats()
    grammar_stats.check("Good grammar.")
    grammar_stats.check("bad grammar.")
    result = grammar_stats.percentage_good()
    assert result == 50

def test_one_out_of_three_correct():
    grammar_stats = GrammarStats()
    grammar_stats.check("bad grammar.")
    grammar_stats.check("worse grammar")
    grammar_stats.check("Good grammar.")
    result = grammar_stats.percentage_good()
    assert result == 33
