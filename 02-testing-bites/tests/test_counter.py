from lib.counter import Counter

def test_counter_initially_report_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

def test_counter_adds_a_single_number():
    counter = Counter()
    counter.add(2)
    result = counter.report()
    assert result == "Counted to 2 so far."

def test_counter_adds_multiple_numbers():
    counter = Counter()
    counter.add(3)
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 8 so far."
