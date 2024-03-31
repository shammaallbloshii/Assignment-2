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
