"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time based on number of layers.
    
    :param number_of_layers: int - number of layers of lasagna.
    :return: int - the total preparation time for the lasagna derived from 'PREPARATION_TIME'.
    
    This function takes the number of layers of lasagna used, and multiplies the amount by
    'PREPARATION_TIME' to find a total number of minutes for each layer being prepared 
    collectively.
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total minutes spent in the kitchen cooking.
    
    :param number_of_layers: int - number of layers of lasagna.
    :param elapsed_bake_time: int - total time the lasagna has spent cooking in the oven.
    "return: int - returns the total amount of time in minutes spent preparing and cooking
    the lasagna.
    
    Function takes the number of layers of lasagna, works out preparation time needed for each layer 
    then adds the time the lasagna has spent in the oven already to output a total time in minutes.
    """
    return (number_of_layers * PREPARATION_TIME) + elapsed_bake_time
