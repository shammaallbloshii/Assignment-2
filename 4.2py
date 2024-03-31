class Artwork:
    """Class to represent an artwork."""
    def __init__(self, id, title, artist, dateOfCreation, historicalSignificance, location):
        self.id = id
        self.title = title
        self.artist = artist
        self.dateOfCreation = dateOfCreation
        self.historicalSignificance = historicalSignificance
        self.location = location

    def __str__(self):
        return f"{self.title} by {self.artist}, created in {self.dateOfCreation}, located at {self.location}. Significance: {self.historicalSignificance}"

class Exhibition:
    """Class to represent a collection of artworks displayed together."""
    def __init__(self, id, name, startDate, endDate, location):
        self._id = id
        self._name = name
        self._startDate = startDate
        self._endDate = endDate
        self._location = location
        self._artworks = []

    def addArtwork(self, artwork):
        self._artworks.append(artwork)

    def removeArtwork(self, artwork):
        try:
            self._artworks.remove(artwork)
        except ValueError:
            print(f"Artwork {artwork} not found in the exhibition.")

    def __str__(self):
        exhibition_details = f"Exhibition ID: {self._id}, Name: {self._name}, Start Date: {self._startDate}, " \
                             f"End Date: {self._endDate}, Location: {self._location}"
        artworks_details = "\nArtworks in the exhibition:\n" + "\n".join(str(artwork) for artwork in self._artworks)
        return exhibition_details + "\n" + artworks_details

# Example usage
if __name__ == "__main__":
    # Create an exhibition
    exhibition1 = Exhibition(id=1, name="Modern Art Showcase",
                             startDate="2024-04-01", endDate="2024-04-15",
                             location="Metropolitan Museum of Art, New York")

    # Create some artworks
    artwork1 = Artwork(id=101, title="Abstract Symphony", artist="Wassily Kandinsky",
                       dateOfCreation="2023", historicalSignificance="Innovative abstract art",
                       location="Gallery A")
    artwork2 = Artwork(id=102, title="Sunset Serenade", artist="Rob Kaz",
                       dateOfCreation="2022", historicalSignificance="Captures natural beauty",
                       location="Gallery B")

    # Add artworks to the exhibition
    exhibition1.addArtwork(artwork1)
    exhibition1.addArtwork(artwork2)

    # Display exhibition details
    print("Exhibition details:")
    print(exhibition1)

    # Remove an artwork
    exhibition1.removeArtwork(artwork1)
    print("Updated exhibition details after removing artwork:")
    print(exhibition1)
