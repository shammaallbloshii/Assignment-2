class Event:
    """Base class to represent events like Tours, SpecialEvents."""
    def __init__(self, id, name, startDate, endDate, location):
        self._id = id
        self._name = name
        self._startDate = startDate
        self._endDate = endDate
        self._location = location

    def schedule(self):
        # Scheduling logic goes here
        pass

    def cancel(self):
        # Cancellation logic goes here
        pass

    def __str__(self):
        return f"Event ID: {self._id}, Name: {self._name}, Start Date: {self._startDate}, " \
               f"End Date: {self._endDate}, Location: {self._location}"

# Example usage:
if __name__ == "__main__":
    event1 = Event(id=1, name="Conference", startDate="2024-04-01", endDate="2024-04-03", location="City Center")
    print(event1)  # Display event details
    event1.schedule()  # Call scheduling logic
    event1.cancel()  # Call cancellation logic

