

class Brand:
    """Band class to manage a collection of musicians."""

    def __init__(self, name=" "):
        """Constrict a band with a name and empty musician list."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a band"""
        return f"{self.name} ({','.join(str(musician) for musician in self.musicians)})"

    def add_musician(self, musician):
        """Add a musician to the band's list of musicians."""
        self.musicians.append(musician)

    def play(self):
        """Have each musician in the band play their instrument."""
        for musician in self.musicians:
            print(musician.play())

