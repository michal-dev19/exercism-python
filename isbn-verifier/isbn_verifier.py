"""Module used to check an ISBN-10 number"""


def is_valid(isbn):
    isbn_int = []
    total = 0

    # handle invalid formats and edge cases
    length = [1 for item in isbn if item.isdigit() or item == "X"]
    if sum(length) != 10:
        return False
    if "X" in isbn and isbn[-1] != "X":
        return False
    if isbn.count("X") > 1:
        return False

    # loop through 'isbn' to make a list of integers to be used for check
    for item in isbn:
        if item == "-":
            continue
        if item.isdigit():
            isbn_int.append(int(item))
        elif item == "X":
            isbn_int.append(10)
        else:
            return False

    # total is compiled for isbn check
    multiplier = 10
    for item in isbn_int:
        total += item * multiplier
        multiplier -= 1

    return total % 11 == 0
