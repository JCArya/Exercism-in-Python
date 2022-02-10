
from math import sqrt, exp, sin, cos
import cmath
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary
    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            oi = other.imaginary
        else:
            oi = 0
        return ComplexNumber(self.real + other.real, self.imaginary + oi)
    def __radd__(self,other):
        return ComplexNumber(self.real + other, self.imaginary)
    def __mul__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other, 0)
        re = self.real * other.real - (self.imaginary * other.imaginary)
        im = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(re, im)
    def __rmul__(self, other):
        other = ComplexNumber(other, 0)
        return other.__mul__(self)
    def __sub__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other, 0)
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
    def __rsub__(self, other):
        other = ComplexNumber(other, 0)
        return other.__sub__(self)
    def __truediv__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other, 0)
        a,b,c,d = self.real, self.imaginary, other.real, other.imaginary
        denom = c*c + d*d
        real = (a*c + b*d)/denom
        imag = (b*c - a*d)/denom
        return ComplexNumber(real, imag)
    def __rtruediv__(self, other):
        other = ComplexNumber(other, 0)
        return other.__truediv__(self)
    def __abs__(self):
        return sqrt(self.real*self.real + self.imaginary*self.imaginary)
    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)
    def exp(self):
        ee = exp(self.real)
        real = ee * cos(self.imaginary)
        imag = ee * sin(self.imaginary)
        return ComplexNumber(real, imag)
    def __repr__(self):
        return f'{self.real} + {self.imaginary}i'