def translate_word(x):
    vowels=['a','e','i','o','u','xr','yt']
    if any(x.startswith(i) for i in vowels):
        return x+'ay'
    for consonant in ['squ', 'sch', 'thr', 'qu', 'ch', 'th', 'y', 'rh']:
        if x.startswith(consonant):
            return x[len(consonant):]+consonant+'ay'
    return x[1:]+x[0]+'ay'
def translate(text):
    return ' '.join( [translate_word(x) for x in text.split() ])
