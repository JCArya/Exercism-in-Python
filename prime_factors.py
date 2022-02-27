""" Prime Factors """
def factors(value):
    prime_factors = []
    factor = 2
    while value > 1:
        if value % factor == 0:
            prime_factors.append(factor)
            value /= factor
        else:
            factor += 1
    return prime_factors