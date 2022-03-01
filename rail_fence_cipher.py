def _listOfIndexes(lenght: int, rails: int) -> list:
    numbers = list()
    x = 0
    kier = rails
    for i in range(lenght):
        numbers.append(x)
        if x < kier:
            x += 1
        if x > kier-1:
            x -= 1
        if x == rails-1:
            kier = 0
        if x == 0:
            kier = rails
    return numbers
def encode(message: str, rails: int) -> str:
    numbers = _listOfIndexes(len(message), rails)
    return "".join(l[1] for i in range(rails)
                   for l in list(zip(numbers, message)) if l[0] == i)
def decode(encoded_message: str, rails: int) -> str:
    numbers = _listOfIndexes(len(encoded_message), rails)
    zipped = list(zip(sorted(numbers), encoded_message))
    decoded = ""
    for i in numbers:
        for l in zipped:
            if l[0] == i:
                decoded += l[1]
                zipped.pop(zipped.index(l))
                break
    return decoded
