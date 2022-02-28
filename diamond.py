from string import ascii_uppercase
def rows(letter):
    result = []
    inx = ascii_uppercase.index(letter)
    result.append("A".center(inx*2+1))
    middle = 1
    for l in ascii_uppercase[1:inx+1]:
        st = l+middle*' '+l
        result.append(st.center(inx*2+1))
        middle += 2
        
    result += reversed(result[:-1])
    return result
