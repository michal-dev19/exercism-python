"""Module to decode and encode a string of characters"""

from itertools import groupby

def decode(string):
    """Decodes a string

    :param string: str - string of characters
    :return: str - compressed data"""

    decoded_string = ''
    number = ''

    for item in string:
        if item.isdigit():
            number += item
        if (item.isalpha() or item.isspace()) and number == '':
            decoded_string += item
        if (item.isalpha() or item.isspace()) and number.isalnum():
            decoded_string += int(number) * item
            number = ''
    return decoded_string

def encode(string):
    """Encodes a string
    
    :param string: str - compressed data
    :return: str - string of uncompressed data"""

    encoded_string = ''
    group = []
    index = 0

    for item, key in groupby(string):
        group.append(len(list(key)))
        if (group[index]) < 2:
            encoded_string += item
        else:
            encoded_string += (str(group[index]) + item)  
        index += 1
    return encoded_string