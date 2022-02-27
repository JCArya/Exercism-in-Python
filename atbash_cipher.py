from textwrap import wrap
ALPHA_LOOKUP = {"a": "z", "b": "y", "c": "x", "d": "w", "e": "v",
                "f": "u", "g": "t", "h": "s", "i": "r", "j": "q",
                "k": "p", "l": "o", "m": "n", "n": "m", "o": "l",
                "p": "k", "q": "j", "r": "i", "s": "h", "t": "g",
                "u": "f", "v": "e", "w": "d", "x": "c", "y": "b",
                "z": "a"}
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
def encode(plain_text) -> str:
    encoded = ""
    for c in plain_text.lower():
        if c.isalpha():
            encoded += ALPHA_LOOKUP[c]
        elif c in DIGITS:
            encoded += c
    
    return " ".join(wrap(encoded, 5))
def decode(ciphered_text) -> str:
    decoded = ""
    for c in ciphered_text:
        if c.isalpha():
            decoded += ALPHA_LOOKUP[c]
        elif c in DIGITS:
            decoded += c
    return decoded