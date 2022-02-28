SMALL_LETTER_START = ord("a")
BIG_LETTER_START = ord("A")
ALPHABET_LETTER_COUNT = 26
def char_convert(current_char: str, rotation_key_in: int) -> str:
    if ("A" <= current_char) and (current_char <= "z"):
        letter_start = BIG_LETTER_START if current_char <= "Z" else SMALL_LETTER_START
        encoded_char = ord(current_char) - letter_start + rotation_key_in
        encoded_char %= ALPHABET_LETTER_COUNT
        return chr(encoded_char + letter_start)
    return current_char
def rotate_naive(text: str, key: int) -> str:
    return "".join([char_convert(x, key) for x in text])
# Stealing/learning from the comunity
from string import ascii_lowercase as al
def rotate(text, key):
    newchars = al[key:] + al[:key]
    trans = str.maketrans(al + al.upper(), newchars + newchars.upper())
    return text.translate(trans)
