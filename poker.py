
my_dict = {
    "One Pair": 2,
    "Two Pair": 3,
    "Three of a Kind": 4,
    "Straight": 5, 
    "Flush": 6,
    "Full House": 7,
    "Four of a Kind": 8,
    "Straight Flush": 9,
    "Five of a Kind": 10
}
my_other_dict = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}
def best_hands(hands):
    scores = []
    tie = []
    
    for hand in hands:
        # Step 1 Pre-process hand
        cards = hand.split(" ")
        score = 0
        card_tups = list(set([tuple((card, sum([1 for candidate in cards if candidate[0] == card[0]]))) for card in cards]))
        
        # Step 2 - Check Repeats
        repeats = list(set([tuple((tup[0][0], tup[1])) for tup in card_tups if tup[1] > 1]))
    
        # Step 3 - Collect Non-repeats for Later Analysis
        one_offs = [tuple((tup[0][0], tup[1])) for tup in card_tups if tup[1] == 1]
        
        # Step 4 - Analyze Repeats
        if len(repeats) > 0:
            if len(repeats) == 2:
                if (repeats[0][1] + repeats[1][1]) == 4:
                    score = my_dict["Two Pair"] + sum([my_other_dict[repeat[0][0]] / 14 for repeat in repeats])
                else:
                    score = my_dict["Full House"] + sum([my_other_dict[repeat[0]] / 14 for repeat in repeats if repeat[1]==3])
                    one_offs = [repeat for repeat in repeats if repeat[1]==2]
            elif repeats[0][1] == 2:
                score = my_dict["One Pair"] + my_other_dict[repeats[0][0]] / 14
            elif repeats[0][1] == 3:
                score = my_dict["Three of a Kind"] + my_other_dict[repeats[0][0]] / 14
            elif repeats[0][1] == 4:
                score = my_dict["Four of a Kind"] + my_other_dict[repeats[0][0]] / 14
            elif repeats[0][1] == 5:
                score = my_dict["Five of a Kind"]
        else:
            #Step 5 - Check Flush
            flush = sum([1 for tup in card_tups if tup[0][-1] == card_tups[0][0][-1]]) == 5
            tie_break_f = sum([my_other_dict[tup[0][0:-1]] for tup in card_tups]) / 60 
            
            #Step 6 - Check Straight
            straight = sorted([my_other_dict[tup[0][0:-1]] for tup in card_tups])
            
            if 2 in straight and 14 in straight:
                straight[straight.index(14)] = 1
                straight = sorted(straight)
            tie_breaker = max(straight) / 14
            straight = sum([(card - straight[idx-1]) == 1 for idx, card in enumerate(straight) if idx > 0]) == 4
            
            # Step 7 - Check whether straight, flush or straight flush
            if straight and flush:
                score = my_dict["Straight Flush"] + tie_breaker
            elif straight:
                score = my_dict["Straight"] + tie_breaker
            elif flush:
                score = my_dict["Flush"] + tie_break_f
            else:
                # Step 8 - Determine High card score
                score = sum([my_other_dict[tup[0][0]] for tup in card_tups]) / 60
        scores.append(score)
        tie.append(one_offs)
    
    # Step 9 - Search to Find Max Scores
    max_value = max(scores)
    indices = [index for index, value in enumerate(scores) if value == max_value]
    
    # If Non-unique use Tie Breaker Information
    if len(indices) == 2 and len(tie) == 2:
        for i, tups in enumerate(tie):
            for tup in tups:
                scores[i] += my_other_dict[tup[0]] / 14
        indices = [scores.index(max(scores))]
    return [hands[ind] for ind in indices]