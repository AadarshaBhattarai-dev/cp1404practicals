"""
CP1404/CP5632 Practical
UnreliableCar class
"""
import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Car that may not drive when requested, depending on reliability."""

    def __init__(self, name, fuel, reliability):
        """
        reliability: float between 0 and 100 representing % chance the drive will succeed.
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if random.random() * 100 < self.reliability:
            return super().drive(distance)
        return 0
