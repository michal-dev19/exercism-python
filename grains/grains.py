"""Module calculates the number of grains of wheat on a chessboard, when starting from 1 grain, each move doubles
the grain"""

NUMBER_OF_SQUARES = 64

def square(number):
    """Calls a specific int to check the number of grains on a given square
    
    :param number: int - number of square
    :return: number of grains on said square"""

    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    
    return 2**(number - 1)
    

def total():
    """Calculates total amount of grain on the chessboard"""
    
    return 2**(NUMBER_OF_SQUARES) - 1