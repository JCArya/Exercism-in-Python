from collections.abc import Iterable
def flatten(iterable):
    elems = (flatten(x) if isinstance(x, Iterable) else [x]
             for x in iterable if x is not None)
    return sum(elems, [])