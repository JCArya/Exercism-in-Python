from re import fullmatch
def is_valid(isbn: str) -> bool:
    res = fullmatch('(\\d)-?(\\d{3})-?(\\d{5})-?(X|\\d)', isbn)
    if res is None:
        return False          
    return not sum(10 if x == 'X' else (10 - i) * int(x) for i, x in enumerate(''.join(res.groups()))) % 11
    

        

          