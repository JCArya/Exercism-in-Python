def primes(limit):
    non_primes = []
    pr = []
    for i in range(2, limit + 1):
        if i not in non_primes:
            pr.append(i)
        for j in range(i, limit + 1, i):
            if j not in pr:
                non_primes.append(j)    
    return pr