"""Module determines if an input is a pangram"""

from string import ascii_lowercase


def is_pangram(sentence):
    """Function takes input and checks if it is a pangram

    Args:
        sentence - str: sentence to be checked
        return - bool: if sentence is verified to be a pangram"""

    return all(item in sentence.lower() for item in ascii_lowercase)
