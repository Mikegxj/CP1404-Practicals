import datetime

class Project:
    """Represents a project with its details."""
    def __init__(self, name, start_date, priority: int, estimate: float, completion: int):
        """Initialize a new Project instance."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __str__(self):
        """Return a string representation of the project with key details."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                 f"priority {self.priority}, estimate: ${self.estimate:,.2f}, "
                 f"completion: {self.completion}%")

    def is_complete(self):
        """Check if the project is complete."""
        return self.completion == 100

    def is_overdue(self):
        """Determine if the project is overdue."""
        return datetime.date.today() > self.start_date and not self.is_complete()

    def __lt__(self, other):
        """Define the less-than comparison for sorting projects based on priority."""
        return self.priority < other.priority

    def __eq__(self, other):
        """Define equality based on project priority."""
        return self.priority == other.priority


