"""Module determines whether a string is an isogram"""


def is_isogram(string):
    """Checks whether the input matches criteria of an isogram

    Args:
        string - str: input word/phrase
        return - bool: true if word is isogram otherwise false"""

    string_set = {item for item in string.lower() if item.isalpha()}
    return len(string_set) == len([item for item in string.lower() if item.isalpha()])
