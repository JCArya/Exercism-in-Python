from math import sqrt
def score(x, y):
    return 10 if (d := sqrt(abs(x) ** 2 + abs(y) ** 2)) <= 1 \
        else 5 if d <= 5 else 1 if d <= 10 else 0
