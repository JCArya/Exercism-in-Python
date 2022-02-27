def classify(number):

    """ A perfect number equals the sum of its positive divisors.
    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
        return
    aliquot = sum(factors(number))

    if aliquot == number:
        
        return "perfect"

    elif aliquot < number:         

        return "deficient"
    return "abundant"

def factors(number):

    s = set()

    for i in range(1, number):

        if number % i == 0:

            s.add(i)
    return s

        

          