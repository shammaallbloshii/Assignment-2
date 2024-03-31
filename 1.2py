class Artwork:
    """Class to represent an individual piece in the museum's collection."""

    def __init__(self, id, title, artist, dateOfCreation, historicalSignificance, location):
        self._id = id
        self._title = title
        self._artist = artist
        self._dateOfCreation = dateOfCreation
        self._historicalSignificance = historicalSignificance
        self._location = location

    def __str__(self):
        return f"ID: {self._id}, Title: {self._title}, Artist: {self._artist}, " \
               f"Date of Creation: {self._dateOfCreation}, Historical Significance: {self._historicalSignificance}, " \
               f"Location: {self._location}"

    def updateLocation(self, newLocation):
        self._location = newLocation

    def displayDetails(self):
        print(self.__str__())


# Example usage
if __name__ == "__main__":
    artwork1 = Artwork(id=1, title="Mona Lisa", artist="Leonardo da Vinci",
                       dateOfCreation="1503-1506", historicalSignificance="Iconic portrait",
                       location="Louvre Museum, Paris")

    print("Artwork details:")
    artwork1.displayDetails()

    # Update location
    artwork1.updateLocation("Metropolitan Museum of Art, New York")
    print(f"Updated location: {artwork1._location}")
