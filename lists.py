
from statistics import mean, median
def get_rounds(number: int) -> list[int]:
    '''
 
     :param number: int - current round number.
     :return: list - current round and the two that follow.
    '''
    return [*range(number, number + 3)]
def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    '''
 
    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    '''
    return rounds_1 + rounds_2
def list_contains_round(rounds: list[int], number: int) -> bool:
    '''
 
    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    '''
    return number in rounds
def card_average(hand: list[int]) -> float:
    '''
 
    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    '''
    return mean(hand)
def approx_average_is_average(hand: list[int]) -> bool:
    '''
 
    :param hand: list - cards in hand.
    :return: bool - approximate average value of the cards in the hand.
    '''
    average = mean(hand)
    approx_average = (hand[0] + hand[-1]) / 2
    
    return average in (approx_average, median(hand))
        
def average_even_is_average_odd(hand: list[int]) -> bool:
    '''
 
    :param hand: list - cards in hand.
    :return: bool - approximate average value of the cards in the hand.
    '''
    even = filter(lambda x: x % 2 == 0, hand)
    odd = filter(lambda x: x % 2 != 0, hand)
    return mean(odd) == mean(even)
def maybe_double_last(hand: list[int]) -> list[int]:
    '''
 
    :param hand: list - cards in hand.
    :return: None - the hand with Jacks (if present) value doubled.
    '''
    if hand[-1] == 11:
        hand[-1] *= 2
        
    return hand