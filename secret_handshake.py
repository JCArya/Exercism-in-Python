def commands(binary_str):
    
    handshakes = ['wink', 'double blink', 'close your eyes', 'jump']

    bin_lists = [x for x in binary_str[1:]][::-1]

    result = [y for x, y in zip(bin_lists, handshakes) if x =='1']

    if binary_str[0] == '1':

        result.reverse()

    return result