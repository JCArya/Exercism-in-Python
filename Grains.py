def square(number):
    if number > 0 and number <= 64:     
        number -= 1
        return 2 ** number
    else:
        raise ValueError("square must be between 1 and 64")
def total():
    return (2 ** 64) - 1
