from lib.music_tracker import *

def test_instance_initialises():
    tracker = MusicTracker()
    assert tracker.list_tracks() == []

def test_add_track():
    tracker = MusicTracker()
    tracker.add('My Song')
    assert tracker.list_tracks() == ['My Song']

def test_multiple_tracks():
    tracker = MusicTracker()
    tracker.add('My Song')
    tracker.add('Another Song')
    assert tracker.list_tracks() == ['My Song', 'Another Song']

def test_empty_string():
    tracker = MusicTracker()
    tracker.add('My Song')
    tracker.add('')
    assert tracker.list_tracks() == ['My Song']

def test_duplicate_track():
    tracker = MusicTracker()
    tracker.add('My Song')
    tracker.add('Another Song')
    tracker.add('My Song')
    tracker.list_tracks() ==  ['My Song', 'Another song', 'My Song']

def test_number_input():
    tracker = MusicTracker()
    tracker.add(5)
    tracker.add(5.9)
    assert tracker.list_tracks() == []