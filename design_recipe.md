# {{PROBLEM}} Class Design Recipe

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

```python
# EXAMPLE

class MusicTracker:
    # User-facing properties:

    def __init__(self):
        self.tracks = []

    def add(self, track):
        # Parameters:
        #   track: string representing a single song
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the track to the self object
        self.tracks.append(track)

    def list_tracks(self):
        # Returns:
        #   A list of tracks
        return self.tracks
```

## 3. Create Examples as Tests

``` python
# EXAMPLE

"""
Check instance initialises
"""
tracker = MusicTracker()
isinstance(tracker, MusicTracker) => True

"""
Add a track
"""
tracker = MusicTracker()
tracker.add('My Song')
tracker.list() => ['My Song']

"""
Add multiple tracks
"""
tracker = MusicTracker()
tracker.add('My Song')
tracker.add('Another Song')
tracker.list() => ['My Song', 'Another song']

"""
Add empty string
"""
tracker = MusicTracker()
tracker.add('My Song')
tracker.add('')
tracker.list() => ['My Song']

"""
Add duplicate tracks
"""
tracker = MusicTracker()
tracker.add('My Song')
tracker.add('Another Song')
tracker.add('My Song')
tracker.list() =>  ['My Song', 'Another song', 'My Song']
```
