"""Module coverts a sequence of digits in one base, representing a number, into a sequence of 
digits in another base, representing the same number"""

def rebase(input_base, digits, output_base):
    """Translates a number in one base to the same number in another base
    
    :param input_base: int - the base being inputted
    :param digits: int - the digits to be translated
    :param output_base: int - the desired base to be outputted"""
    # test for inputs
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    for digit in digits:
        if input_base <= digit or digit < 0:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        
    
    # loop for finding the actual value of the digits with the input base
    digit_value = 0
    iterator = len(digits) - 1
    for digit in digits:
        digit_value += (digit * input_base**iterator)
        iterator -= 1

    # check if digit_value = 0, if so return it in a list
    output_base_value = []
    if digit_value == 0:
        output_base_value.append(0)
        return output_base_value
    
    # loop to find the number using the output base
    while digit_value > 0:
        output_base_value.append(digit_value % output_base)
        digit_value = digit_value // output_base

    # reverses and joins all the digits into one variable
    output_base_value.reverse()
    return output_base_value