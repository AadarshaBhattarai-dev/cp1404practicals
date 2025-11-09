"""CP1404 Practical 07"""

class Guitar:

    def __init__(self, name: str, year: int, cost: float):
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        return f"{self.name}, {self.year}, ${self.cost:,.2f}"

    def __repr__(self):
        return f"Guitar({self.name!r}, {self.year}, {self.cost})"

    def is_vintage(self):
        from datetime import datetime
        current_year = datetime.now().year
        return (current_year - self.year) >= 30

    def __lt__(self, other):
        return self.year < other.year
