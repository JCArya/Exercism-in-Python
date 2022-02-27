def is_anagrams(target: str, word: str):

        

          

    if target == word:

        

          

        return False

        

          

    for c in set(target):

        

          

        if target.count(c) != word.count(c):

        

          

            return False

        

          

    return True

        

          

def find_anagrams(word: str, candidates: list):

        

          

    anagrams = []

        

          

    word = word.lower()

        

          

    len_target = len(word)

        

          

    for candidate in candidates:

        

          

        if len(candidate) == len_target and is_anagrams(word, candidate.lower()):

        

          

            anagrams.append(candidate)

        

          

    return anagrams