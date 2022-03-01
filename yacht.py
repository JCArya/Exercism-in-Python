# Score categories.
# Change the values as you see fit.
YACHT = 'BIG'
ONES = 'ones'
TWOS = 'twos'
THREES = 'threes'
FOURS = 'fours'
FIVES = 'fives'
SIXES = 'sixes'
FULL_HOUSE = 'FH'
FOUR_OF_A_KIND = 'FK'
LITTLE_STRAIGHT = 'LS'
BIG_STRAIGHT = 'BS'
CHOICE = 'choice'
def score(dice, category):
    temp = 0
    if category == 'ones':
        temp = sum(x for x in dice if x == 1)
    if category == 'twos':
        temp = sum(x for x in dice if x == 2)
    if category == 'threes':
        temp = sum(x for x in dice if x == 3)
    if category == 'fours':
        temp = sum(x for x in dice if x == 4)
    if category == 'fives':
        temp = sum(x for x in dice if x == 5)
    if category == 'sixes':
        temp = sum(x for x in dice if x == 6)
    if category == 'FH':
        dice.sort()
        if len(set(dice)) != 2:
            return temp
        if dice[0] == dice[1] and dice[2] == dice[4] or dice[4] == dice[3] and dice[2] == dice[0]:
            temp = sum(dice)
        else:
            pass
    if category == 'FK':
        dice.sort()
        if dice[0] == dice[3] or dice[4] == dice[1]:
            temp = dice[3] * 4
    if category == 'LS':
        a = [1, 2, 3, 4, 5]
        if a == sorted(dice):
            temp = 30
        else:
            temp = 0
    if category == 'BS':
        a = [2, 3, 4, 5, 6]
        if a == sorted(dice):
            temp = 30
        else:
            pass
    if category == 'choice':
        temp = sum(dice)
    if category == 'BIG':
        if len(set(dice)) == 1:
            temp = 50
        
    return temp