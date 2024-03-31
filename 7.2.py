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

# Example usage
if __name__ == "__main__":
    # Create a sample ticket
    sample_ticket = Ticket(id=1, event="Art Exhibition", price=20, date="2023-05-15", visitorId=123, location="Gallery A")

    # Print ticket details
    print(sample_ticket)
