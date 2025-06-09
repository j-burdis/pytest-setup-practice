from lib.music_library import MusicLibrary
from lib.track import Track

def test_add_method_appends_a_track():
    music_library = MusicLibrary()
    track = Track("Local Hero", "Mark Knopfler")
    music_library.add(track)
    assert music_library.tracks == [track]

def test_add_method_appends_multiple_tracks():
    music_library = MusicLibrary()
    track1 = Track("Local Hero", "Mark Knopfler")
    track2 = Track("Brothers In Arms", "Dire Straits")
    music_library.add(track1)
    music_library.add(track2)
    assert music_library.tracks == [track1, track2]

def test_search_keyword_returns_correct_list():
    music_library = MusicLibrary()
    track1 = Track("Local Hero", "Mark Knopfler")
    track2 = Track("Brothers in Arms", "Dire Straits")
    music_library.add(track1)
    music_library.add(track2)
    assert music_library.search("Arms") == [track2]

def test_search_keyword_returns_empty_list_no_match():
    music_library = MusicLibrary()
    track1 = Track("Local Hero", "Mark Knopfler")
    music_library.add(track1)
    assert music_library.search("Arms") == []