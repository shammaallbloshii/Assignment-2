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
        self._artworks.remove(artwork)

    def __str__(self):
        return f"Exhibition ID: {self._id}, Name: {self._name}, Start Date: {self._startDate}, " \
               f"End Date: {self._endDate}, Location: {self._location}"
