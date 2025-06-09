from lib.track import Track

def test_creates_title_and_artist_as_strings():
    track = Track("Local Hero", "Mark Knopfler")
    assert track.title == "Local Hero"
    assert track.artist == "Mark Knopfler"

def test_matches_method_returns_true_for_matches():
    track = Track("Local Hero", "Mark Knopfler")
    assert track.matches("Local Hero") == True

def test_matches_method_for_none_match():
    track = Track("Local Hero", "Mark Knopfler")
    assert track.matches("Local Zero") == False