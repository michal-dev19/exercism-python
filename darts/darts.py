import math

"""Module for scoring a dart on a 10 point circle"""

def score(x, y):
    """Determine the score of a dart landing on a 10 point circle
    
    :param x: int - the x coordinate of the dart
    :param y: int - the y coordinate of the dart
    :return: int - the score of the dart depending on the band landed in
    """
    inner_band_distance = 1
    middle_band_distance = 5
    outer_band_distance = 10
    distance = math.sqrt(x**2 + y**2)

    if distance <= inner_band_distance:
        return 10
    if distance <= middle_band_distance:
        return 5
    if distance <= outer_band_distance:
        return 1
    return 0