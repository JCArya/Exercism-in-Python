
from heapq import nlargest
def latest(scores):
    return scores[-1]
def personal_best(scores):
    return max(scores, default=None)
def personal_top_three(scores):
    return nlargest(3, scores)