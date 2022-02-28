
import string
from math import sqrt
def cipher_text(plain_text):
    clean_text = ""
    text_square = ""
    res = ""
    for i in plain_text:
        if i in string.ascii_letters or i in string.digits:
            clean_text += i.lower() 
    if len(clean_text) > 4:
        sqroot = round(sqrt(len(clean_text)))
        if int(sqroot**2) >= len(clean_text):
            col = sqroot
            row = sqroot
        elif int(sqroot**2) < len(clean_text):
            col = sqroot + 1
            row = sqroot
        for i in range(col):
            for j in range(row):
                text_square += clean_text.ljust(row*col)[(j*col)+i]
        for i in range(1, col+1):
            res += text_square[(i-1)*row:row*i].ljust(row)+" " 
        return res[0:-1]
    else:
        return clean_text
