# You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.
#
# A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).
#
# The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

class MyCalendar:

    def __init__(self):
        # Initialize an empty list to store the events
        self.events = []

    def book(self, start: int, end: int) -> bool:
        # Check for overlap with existing events
        for s, e in self.events:
            # If the new event overlaps with any existing event
            if not (end <= s or start >= e):  # No overlap condition: (new_end <= old_start) or (new_start >= old_end)
                return False
        # If no overlap, add the event
        self.events.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)