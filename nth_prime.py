
def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
    prime_lst = []
    count = 2
    while len(prime_lst) != number:
        if len(prime_lst) != 0:
            for item in prime_lst:
                if count%item == 0:
                    break
                if item == prime_lst[-1]:
                    prime_lst.append(count)
        else:
            prime_lst.append(count)
        count += 1
    return prime_lst[-1]
        