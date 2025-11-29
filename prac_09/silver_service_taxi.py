"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi with fanciness multiplier and flagfall."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return fare including flagfall, rounded to nearest 10c via Taxi.get_fare logic."""
        base_fare = super().get_fare()
        return round(base_fare + self.flagfall, 1)

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
