
        

          

def largest(max_factor, min_factor=0):

        

          

    """

        

          

    :param min_fact: int of the smallest number in the range

        

          

    :param max_fact: int of the largest number in the range

        

          

    return: int, list of largest palindrome in the range and list of factors

        

          

    """

        

          

    if max_factor < min_factor:

        

          

        raise ValueError("min must be <= max")

        

          

    prod = products(min_factor, max_factor, False)

        

          

    if prod is None:

        

          

        return None, []
    return prod, factors(prod, min_factor, max_factor)
def smallest(max_factor, min_factor = 0):
    """
    :param min_fact: int of the smallest number in the range
    :param max_fact: int of the largest number in the range
    return: int, list of smallest palindrome in the range and list of factors
    """
    if max_factor < min_factor:
        raise ValueError("min must be <= max")
    prod = products(min_factor, max_factor, True)
    if prod is None:
        return None, []
    return prod, factors(prod, min_factor, max_factor)
def products(min_fact, max_fact, minimum):
    """
    :param min_fact: the minimum range for the products
    :param max_fact: the maximum range for the products
    :param minimum: bool to check if minimum or maximum palindrome is neede
    return: the smallest/largest palindrome in the range
    """
    if min_fact == max_fact == 0:
    	return 0
    elif minimum:

    	length = range(min_fact**2, max_fact**2+1)
    else:
    	length = reversed(range(min_fact**2-1, max_fact**2))
    if min_fact == 0: #To prevent modulo by 0, still works because 0//num will equal 0, which is in range.
        min_range = 1

    else:
        min_range = min_fact 
    for i in length:
        if palin(i) and any(min_fact <= i//j <= max_fact for j in range(min_range, max_fact + 1) if i % j == 0): #This checks if the number is a palindrome and if there's a set of factors within the given range
            return i
    return None
def palin(num):
    """
    :param num: int to check if palindrome
    :return: bool if palindrome
    """
    return str(num) == str(num)[::-1]
def factors(num, min_fact, max_fact):
    """
    :param num: int of the palindrome     
    :param min_fact: the minimum range for factor
    :param max_fact: the maximum range for factors
    :return: list of factors of num that is within the range
    """
    if num == 0:
        return [0,1]
    if min_fact != 0:
        return [[i, num//i] for i in range(min_fact, max_fact+1) if num % i == 0 and min_fact <= i <= num//i <= max_fact ]
    else:
        return [[i, num//i] for i in range(min_fact+1, max_fact+1) if num % i == 0 and min_fact <= i <= num//i <= max_fact]