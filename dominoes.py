from typing import *
import itertools
def can_chain(dominoes: List[Tuple[int, int]]) -> Optional[List[Tuple[int, int]]]:
    if not (dominoes := sorted(tuple(sorted(domino)) for domino in dominoes)): return []
    def flip_tuple(tuple_: Tuple[int, int], is_flip: bool) -> Tuple[int, int]:
        return tuple_[::-1] if is_flip else tuple_
    def is_chain(check_data: List[Tuple[int, int]]):
        if check_data[0][0] != check_data[-1][-1]: return False
        iterator = iter(check_data)
        prev = next(iterator)
        while cur := next(iterator, None):
            if prev[-1] != cur[0]: return False
            prev = cur
        return True
    for combo in itertools.permutations(dominoes):
        for flips in itertools.product((True, False), repeat=len(combo)):
            if is_chain(trial := list(map(flip_tuple, combo, flips))): return trial
    return None
