class Ticket:
    def __init__(self, id, event, price, date, visitorId, location):
        self._id = id
        self._event = event
        self._price = price
        self._date = date
        self._visitorId = visitorId
        self._location = location

    def calculatePrice(self):
        # Price calculation logic goes here
        pass

    def __str__(self):
        return f"Ticket ID: {self._id}, Event: {self._event}, Price: ${self._price}, Date: {self._date}, Visitor ID: {self._visitorId}, Location: {self._location}"

class Visitor:
    def __init__(self, id, name, age, category, nationalID):
        self._id = id
        self._name = name
        self._age = age
        self._category = category
        self._nationalID = nationalID

    def purchaseTicket(self, event):
        # Assume price calculation mechanism exists
        return Ticket(id=None, event=event["name"], price=0, date="YYYY-MM-DD", visitorId=self._id, location=event["location"])

    def __str__(self):
        return f"Visitor ID: {self._id}, Name: {self._name}, Age: {self._age}, Category: {self._category}, National ID: {self._nationalID}"

# Example usage
if __name__ == "__main__":
    # Create a visitor
    visitor1 = Visitor(id=1, name="John Doe", age=30, category="Adult", nationalID="1234567890")

    # Assume an event object exists (replace with actual event details)
    event_details = {"name": "Art Exhibition", "location": "Gallery A"}

    # Purchase a ticket
    ticket = visitor1.purchaseTicket(event=event_details)

    # Print visitor details
    print(visitor1)
    print(f"Ticket details: {ticket}")


