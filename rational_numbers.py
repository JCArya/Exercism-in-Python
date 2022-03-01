from __future__ import division
class Rational(object):
    """Implements a Rational number object"""
    def __init__(self, n, d):
        if (d == 0):
            raise ValueError("Denominator cannot be 0")
        if not (isinstance(n, int) and isinstance(d, int)):
            raise ValueError("Numerator and Denominator have to be integers")
        self.n = n
        self.d = d
        self.reduce()
    @staticmethod
    def gcd(a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        return Rational.gcd(b, a % b)
    def reduce(self):
        """simplify given rational number"""
        div = Rational.gcd(self.n, self.d)
        self.n //= div
        self.d //= div
        return self
    def __eq__(self, other):
        return self.n == other.n and self.d == other.d
    def __repr__(self):
        return '{}/{}'.format(self.n, self.d)
    def __add__(self, other):
        return Rational(self.n * other.d + other.n * self.d,
                        (self.d * other.d))
    def __sub__(self, other):
        return Rational(self.n * other.d - other.n * self.d,
                        (self.d * other.d))
    def __mul__(self, other):
        return Rational(self.n * other.n, self.d * other.d)
    def __truediv__(self, other):
        return Rational(self.n * other.d, self.d * other.n)
    def __abs__(self):
        if self.n < 0:
            self.n *= -1
        if self.d < 0:
            self.d *= -1
        return self
    def __pow__(self, power):
        if power > 0:
            return Rational(self.n ** power, self.d ** power)
        return Rational(self.d ** (-1 * power), self.n ** (-1 * power))
    def __rpow__(self, base):
        return pow(base ** self.n, 1/self.d)