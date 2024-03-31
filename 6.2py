class Event:
    """Class to represent a general event."""
    def __init__(self, id, name, startDate, endDate, location):
        self.id = id
        self.name = name
        self.startDate = startDate
        self.endDate = endDate
        self.location = location

class Visitor:
    """Class to represent a visitor."""
    def __init__(self, name):
        self.name = name

class Tour(Event):
    """Class to represent a guided tour, inheriting from Event."""
    def __init__(self, id, name, startDate, endDate, location, guideName, visitorLimit):
        super().__init__(id, name, startDate, endDate, location)
        self.guideName = guideName
        self.visitorLimit = visitorLimit
        self.bookedVisitors = []

    def book(self, visitor):
        if len(self.bookedVisitors) < self.visitorLimit:
            self.bookedVisitors.append(visitor)
            print(f"Visitor {visitor.name} booked for tour {self.name}.")
        else:
            print("Sorry, the tour is fully booked.")

    def cancelBooking(self, visitor):
        try:
            self.bookedVisitors.remove(visitor)
            print(f"Booking for visitor {visitor.name} cancelled for tour {self.name}.")
        except ValueError:
            print("Visitor not found in booking.")

# Example usage
if __name__ == "__main__":
    # Create a tour
    tour1 = Tour(id=1, name="Historical Landmarks Tour",
                 startDate="2024-05-01", endDate="2024-05-15",
                 location="Downtown City", guideName="John Doe", visitorLimit=10)

    # Create some visitors
    visitor1 = Visitor(name="Alice Smith")
    visitor2 = Visitor(name="Bob Johnson")

    # Book visitors for the tour
    tour1.book(visitor1)
    tour1.book(visitor2)

    # Attempt to cancel a booking
    tour1.cancelBooking(visitor1)
