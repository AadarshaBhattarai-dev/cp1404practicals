"""
CP1404 Practical
Testing code using assert and doctest
"""
import doctest
from prac_06.car import Car

def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)

def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length

def format_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a single full stop.
    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_sentence('this is a test')
    'This is a test.'
    """
    formatted = phrase[0].upper() + phrase[1:] if len(phrase) > 0 else phrase

    if not formatted.endswith('.'):
        formatted += '.'

    return formatted

def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    car = Car()
    assert car.fuel == 0, "Car does not set default fuel correctly"

    car = Car(fuel=10)
    assert car.fuel == 10, "Car does not set fuel correctly when passed as parameter"

    print("All assert tests passed!")

run_tests()
doctest.testmod()