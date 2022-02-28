
def decode(string):
    if string == '':
        return ''
    
    output = ''
    new_string = []
    tmp = ''
    for c in string:
        if c.isdigit():
            tmp += c
        else:
            if tmp != '':
                new_string.append(tmp)
                tmp = ''
            new_string.append(c)
        
    string = new_string
    
    i = 0
    while i < len(string):
        c = string[i]
        
        if c.isdigit():
            char = string[i + 1]
            output += int(c) * char
            i += 1
        else:
            output += string[i]
        i += 1
    return output
def encode(string):
    if string == '':
        return ''
    
    pairs = []
    previous_c = string[0]
    counter = 0
    for c in string:
        if c == previous_c:
            counter += 1
        else:
            pairs.append([counter, previous_c])
            counter = 1
        previous_c = c
    pairs.append([counter, previous_c])
        
    output = ''
    for pair in pairs:
        if pair[0] == 1:
            output += pair[1]
        else:
            output += str(pair[0]) + pair[1]
        
    return output
