def three_number(num):
    print("innn")
    teen = {"10":"ten", "11":"eleven", "12":"twelve", "13": "thirteen", "14":"fourteen", "15": "fifteen",\
            "16":"sixteen", "17":"seventeen","18":"eighteen","19":"nineteen"}
    numbers = {"0":"zero", "1":"one", "2":"two", "3":"three","4":"four","5":"five",\
               "6":"six","7":"seven","8":"eight","9":"nine"}
    num_10 = {"2":"twenty","3":"thirty", "4":"forty", "5":"fifty","6":"sixty","7":"seventy",\
              "8":"eighty", "9":"ninety"}
    
    num = "".join(token.lstrip('0') for token in num.split()) if num != "0" else "0"
    #print(num12)
    if len(num) == 3:
        num12 = eval("".join(token.lstrip('0') for token in num[1:].split())) if num[1:] != "00" else 0
        #print("heeeeey")
        #print(num12)
        if num12 == 0:
            return numbers[num[0]]+" hundred"
        elif  num12 < 10:
            return numbers[num[0]]+" hundred "+numbers[num[2]]
        elif num12 >= 10:
            #print("heeeey")
            if num12 < 20:
                return numbers[num[0]]+" hundred "+teen[num[1:]]
            else:
                return numbers[num[0]]+" hundred "+num_10[num[1]] if num12%10 == 0 else numbers[num[0]]+" hundred "+num_10[num[1]]+"-"+numbers[num[2]] 
        
    elif len(num) == 2:
        print(num)
        if num[0] == "1":
            return teen[num]
        else:
            return num_10[num[0]] if eval(num)%10 == 0 else num_10[num[0]]+"-"+numbers[num[1]]
    elif len(num) == 1:
        return numbers[num]
def say(number):
    if number <0 or number >999999999999: raise ValueError("input out of range")
    str_number = "{:,}".format(number)
    strn_list = str_number.split(",")
    strn_list = strn_list[::-1]
    print(strn_list)
    dictn = {"0":"", "1": "thousand", "2":"million", "3": "billion"}
    num = ""
    numsay = []
    #
    for i in range(len(strn_list)-1, -1 , -1 ):
        if strn_list[i] != "000" :            
            nums = three_number(strn_list[i])
            print(nums, i, dictn[str(i)])
            if i != len(strn_list) - 1:
                num  += " " +nums + " " + dictn[str(i)]
            else:
                print("hiii")
                num  += nums + " " + dictn[str(i)]
    return num.rstrip()