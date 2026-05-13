"""Module takes a number and finds the amount of steps to reach the number 1"""

def steps(number):
    """Determines number of steps to reach 1 from any positive integer
    
    If the number is EVEN, divide the number by 2
    If the number is ODD, multiply the number by 3, and add 1
    Repeating this process will, eventually, lead any positive integer to 1
    
    :param number: int - a positive integer
    :return: int - number of steps to reach 1"""
    
    steps_counter = 0

    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    while number != 1:
        if number % 2 == 0:
            number /= 2
            steps_counter += 1
        else:
            number = (number * 3) + 1
            steps_counter += 1
    return steps_counter
