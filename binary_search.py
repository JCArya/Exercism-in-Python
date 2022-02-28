def find(a, x):
    hi = len(a)
    lo = 0
    while lo < hi:
        i = (lo + hi) // 2
        if a[i] < x:
            lo = i + 1
        elif a[i] > x:
            hi = i
        elif a[i] == x:
            return i
    raise ValueError("value not in array")
