from lib.gratitudes import Gratitudes

def test_initially_returns_no_list():
    gratitude = Gratitudes()
    assert gratitude.format() == "Be grateful for: "

def test_multiple_items_concatenated_correctly():
    gratitude = Gratitudes()
    gratitude.add("family")
    gratitude.add("friends")
    gratitude.add("food")
    assert gratitude.format() == "Be grateful for: family, friends, food"
