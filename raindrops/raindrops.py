"""Module converts a number to its corresponding raindrop sounds"""

def convert(number):
    """Determines if 'number' is divisible by 3, or 5, or 7 and matches output accordingly
    
    :param number: int - given number
    :return: string - the result string of 'sounds' or the original number as a string"""

    final_string = ""

    if number % 3 == 0:
        final_string += "Pling"
    if number % 5 == 0:
        final_string += "Plang"
    if number % 7 == 0:
        final_string += "Plong"
    if final_string == "":
        return str(number)
    return final_string
    
    