
def recite(start_verse: int, end_verse: int) -> list:
    """
    :param start_verse: int
    :param end_verse: int
    :return: list of verses
    """
    def create_gifts(day: int) -> str:
        result = items[1]
        if day == 1:
            return result
        
        result = f'and {result}'
        for i in range(2, day + 1):
            result = f'{items[i]}, {result}'
        return result
            
    days = {1 : 'first', 2 : 'second', 3 : 'third', 4 : 'fourth', 5 : 'fifth', 6 : 'sixth', 7 : 'seventh', 8 : 'eighth', 9 : 'ninth', 10 : 'tenth', 11 : 'eleventh', 12 : 'twelfth'}
    items = {1 : 'a Partridge in a Pear Tree', 2 : 'two Turtle Doves', 3 : 'three French Hens', 4 : 'four Calling Birds', 5 : 'five Gold Rings', 6 : 'six Geese-a-Laying', 7 : 'seven Swans-a-Swimming', 8 : 'eight Maids-a-Milking', 9 : 'nine Ladies Dancing', 10 : 'ten Lords-a-Leaping', 11 : 'eleven Pipers Piping', 12 : 'twelve Drummers Drumming'}
    return [f'On the {days[i]} day of Christmas my true love gave to me: {create_gifts(i)}.' 
            for i in range(start_verse, end_verse + 1)]
