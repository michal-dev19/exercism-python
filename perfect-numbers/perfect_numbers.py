from math import sqrt

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    factors = set()

    # !!!IMPORTANT LOGIC!!!
    # doing work up to a midpoint/root and mirroring the result
    # avoiding looping through the entire sequence
    # SAVES MEMORY AND TIME
    for i in range(1, int(sqrt(number)) + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number // i)

    factors.discard(number)
    sum_of_factors = sum(factors)

    if sum_of_factors == number:
        return 'perfect'
    if sum_of_factors > number:
        return 'abundant'
    return 'deficient'