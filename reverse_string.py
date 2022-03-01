def reverse(text):
    rstr1 = ''
    index = len(text)
    while index > 0:
        rstr1 += text[ index - 1 ]
        index = index - 1
    return rstr1
    
