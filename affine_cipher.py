
from math import gcd
oa, m = ord('a'), 26
def encode(plain_text, a, b):
    encode_int = lambda x, a, b: (a * x + b) % m
    group = lambda s: ' '.join(s[i:i + 5] for i in range(0, len(s), 5))
    plain_text = clean(plain_text, a)
    return group(''.join(chr(encode_int(ord(c) - oa, a, b) + oa) if c.isalpha() else c for c in plain_text))
def decode(ciphered_text, a, b):
    decode_int = lambda y, a, b: (pow(a, -1, m) * (y - b)) % m
    ciphered_text = clean(ciphered_text, a)
    return ''.join(chr(decode_int(ord(c) - oa, a, b) + oa) if c.isalpha() else c for c in ciphered_text)
def clean(plain_text, a):
    if gcd(a, m) >= 2: raise ValueError('a and m must be coprime.')
    return ''.join(filter(str.isalnum, plain_text.lower()))