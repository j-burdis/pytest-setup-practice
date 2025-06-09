from lib.music_library import MusicLibrary
from unittest.mock import Mock

def test_initially_library_is_empty_list():
    music_library = MusicLibrary()
    assert music_library.tracks == []

def test_library_adds_tracks_with_mocks():
    music_library = MusicLibrary()
    fake_track1 = Mock("Local Hero", "Mark Knopfler")
    fake_track2 = Mock("Brothers in Arms", "Dire Straits")
    music_library.add(fake_track1)
    music_library.add(fake_track2)
    assert music_library.tracks == [fake_track1, fake_track2]

def test_library_searches_for_keyword_in_mocks():
    music_library = MusicLibrary()
    fake_track1 = Mock()
    fake_track1.matches.return_value = False
    fake_track2 = Mock()
    fake_track2.matches.return_value = True
    music_library.add(fake_track1)
    music_library.add(fake_track2)
    assert music_library.search("Arms") == [fake_track2]