
"""
Variable Length Quantity problem at exercism.com
"""
def encode(numbers):
    """
    Encode numbers using Variable length quantity
 
    Args:
        numbers ([list]): [list of numbers to encode]
 
    Returns:
        [list]: [list of encoded numbers]
    """
    values = []
    # loop numbers in list
    for number in numbers:
        # if number smaller than 128 append directly to values list
        if number < 128:
            values.append(number)
        else:
            # convert number to binary
            binary_number = format(number, "b")
            temp_values = []
            # loop till binary number empty
            while binary_number != "":
                # first slice add 0
                if not temp_values:
                    temp_values.insert(0, int("0" + binary_number[-7:], 2))
                    binary_number = binary_number[:-7]
                # if remaining slice equal or longer than 7 append 1 at the begining of slice
                elif len(binary_number) >= 7:
                    temp_values.insert(0, int("1" + binary_number[-7:], 2))
                    binary_number = binary_number[:-7]
                # if remaining slice shorter than 7 pad with 0 than add 1
                else:
                    temp_values.insert(0,\
                        int("1" + "0"* (7 - len(binary_number)) + binary_number, 2))
                    binary_number = binary_number[:-7]
            values.extend(temp_values)
    return values
def decode(bytes_):
    """
    Decode encoded numbers with Variable Length Quantity
 
    Args:
        bytes_ ([list]): [list of encoded numbers]
 
    Raises:
        ValueError: [if number > 127 and only one number present raise error]
 
    Returns:
        [list]: [list of decoded numbers]
    """
    values = []
    temp_value = ""
    for number in bytes_:
        # if number smaller than 128 and list length 1 append directly to values list
        if number < 128 and len(bytes_) == 1:
            values.append(int(number))
        elif number > 127 and len(bytes_) == 1:
            raise ValueError("incomplete sequence")
        else:
            # convert number to binary format
            binary_number = format(number%128, "07b")
            temp_value += binary_number
            # if number smaller than 128 append temp_value as integer to values
            # and create new empty temp_value
            if number < 128:
                values.append(int(temp_value, 2))
                temp_value = ""
    return values
