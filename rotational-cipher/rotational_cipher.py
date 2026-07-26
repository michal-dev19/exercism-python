from string import ascii_lowercase

ALPHABET_LENGTH = 26


def rotate(text, key):

    new_text = ""
    upper = False

    for index, ch in enumerate(text):
        if ch.isupper():
            upper = True
        elif ch.isspace():
            new_text += " "
            continue
        elif ch.isalpha() is not True:
            new_text += ch
            continue

        index = ascii_lowercase.find(str.lower(ch))
        new_index = (index + key) % ALPHABET_LENGTH

        if upper is True:
            new_text += str.upper(ascii_lowercase[new_index])
        else:
            new_text += ascii_lowercase[new_index]
        upper = False

    return new_text
