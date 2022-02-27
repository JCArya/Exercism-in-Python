def sum_of_multiples(limit, multiples):
    sum = 0
    for item in range(limit):
        for multiple in multiples:
            if multiple != 0 and item%multiple == 0:
                sum += item
                break
    return sum
