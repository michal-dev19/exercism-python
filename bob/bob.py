"""Module for bob"""

def response(hey_bob):
    """Determine the answer bob will provide based on inputted text
    
    :param hey_bob: string - something said to bob
    :return: string - bob's response"""

    hey_bob = hey_bob.strip()

    if hey_bob.isupper() and hey_bob.endswith('?'):
        return "Calm down, I know what I'm doing!"
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if hey_bob.endswith('?'):
        return "Sure."
    if hey_bob.isspace() or hey_bob == '':
        return "Fine. Be that way!"
    return "Whatever."
