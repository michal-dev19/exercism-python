"""Module to determine whether a given year is a leap year or not"""

def leap_year(year):
    """Verifies the given year to either be a leap year or not
    
    :param year: int - the given year
    :return: bool - true if the year is leap, false if not"""

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False