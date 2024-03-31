class Visitor:
    """Class to represent a visitor to the museum."""
    def __init__(self, id, name, age, category, nationalID):
        self._id = id
        self._name = name
        self._age = age
        self._category = category
        self._nationalID = nationalID

    def purchaseTicket(self, event):
        # Simplified, assumes Ticket class exists and price calculation mechanism
        return Ticket(id=None, event=event, price=0, date="YYYY-MM-DD", visitorId=self._id, location=event._location)

    def __str__(self):
        return f"Visitor ID: {self._id}, Name: {self._name}, Age: {self._age}, Category: {self._category}, " \
               f"National ID: {self._nationalID}"
