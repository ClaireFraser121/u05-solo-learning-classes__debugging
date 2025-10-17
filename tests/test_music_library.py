from lib.music_library import MusicLibrary
"""
Initially
There are no tracks
"""
def test_initially_has_no_tracks():
    music_library = MusicLibrary()
    assert music_library.all() == []
