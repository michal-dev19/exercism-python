"""This module determines whether a number is an Armstrong number"""

def is_armstrong_number(number):
    """Determine whether the input 'number' is an Armstrong number
    
    :param number: int - input number
    :return: bool - if the specified number matches the criteria to be an Armstrong number
    
    For a number to be an Armstrong number, the sum of its own digits each raised to the power of the number
    of digits must equal the original number"""

    num_length = len(str(number))
    return sum([int(digit)**num_length for digit in str(number)]) == number
    