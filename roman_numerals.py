
def roman(number):
    num_roman = {1:'I',5:'V', 10:'X',50:'L',100:'C',500:'D',1000:'M'}
    roman = ""
   
    while number>0:   
        place_val = 10**(len(str(number))-1) 
        num = number-(number%place_val) 
        digit = num//place_val 
        if digit<4:
            roman += num_roman[num//digit] * digit
        elif (digit+1)%5==0: 
            roman+= num_roman[num//digit] + num_roman[(digit+1)*place_val]
        elif digit%5==0:
            roman+= num_roman[num]
        elif digit<10: #70 50 + 10 + 10    #7 5 + 1 + 1
            roman+=num_roman[5*place_val]+(num_roman[num//digit]*(digit%5))
        place_val = place_val//10
        number -= num #34
    return roman