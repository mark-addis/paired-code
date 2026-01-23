class MusicTracker():
    def __init__(self):
        self.tracks = []

    def add(self, track):
        if track and isinstance(track, str):
            self.tracks.append(track)

    def list_tracks(self):
        return self.tracks