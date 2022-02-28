
"""Exercism: all your base."""
from collections import deque
from typing import Any, List, NewType
TBase = NewType("TBase", int)
TDigit = NewType("TDigit", int)
TDigits = NewType("TDigits", List[TDigit])
def rebase(input_base, digits, output_base) -> TDigits:
    """Rebase `digits` from `input_base` to `output_base`."""
    input_base = validated_base(input_base, "input")
    output_base = validated_base(output_base, "output")
    return to_base(output_base, from_base(input_base, digits))
def validated_base(base: Any, name: str) -> TBase:
    """Check `base` raising ValueError if invalid."""
    if isinstance(base, int) and base > 1:
        return TBase(base)
    raise ValueError(f"{name} base must be >= 2")
def validated_digit(base: TBase, digit: Any) -> TDigit:
    """Check `digit` to be valid in `base`, raising ValueError accordingly."""
    if isinstance(digit, int) and 0 <= digit < base:
        return TDigit(digit)
    raise ValueError("all digits must satisfy 0 <= d < input base")
def to_base(base: TBase, number: int) -> TDigits:
    """Convert a `number` into a list of digits in `base`."""
    digits: deque[TDigit] = deque()
    while number > 0:
        number, r = divmod(number, base)
        digits.appendleft(TDigit(r))
    return TDigits(list(digits) or [TDigit(0)])
def from_base(base: TBase, digits: TDigits) -> int:
    """Convert `digits` in `base` to a number."""
    number = 0
    multiplier = 1
    for digit in reversed(digits):
        number += multiplier * validated_digit(base, digit)
        multiplier *= base
    return number