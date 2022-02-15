def abbreviate(words: str) -> str:
    for c in '-_':
        words = words.replace(c, ' ')
    return ''.join([word[0] for word in words.upper().split()])