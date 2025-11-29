"""
CP1404/CP5632 Practical
Band class (association: Band has Musicians)
"""
class Band:
    """A Band contains Musicians."""

    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a Musician instance to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return a single-line representation similar to the prac example."""
        members = ", ".join(str(m) for m in self.musicians)
        return f"{self.name} ({members})"

    def play(self):
        """Call a play-like method on each musician (if implemented)."""
        for m in self.musicians:
            try:
                m.play()
            except AttributeError:
                print(m)
