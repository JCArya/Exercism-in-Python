
def is_mine(minefield, x, y):
    return (y >= 0 and y < len(minefield) and
            x >= 0 and x < len(minefield[y]) and
            minefield[y][x] == '*')
def count_mines(minefield, x, y):
    return sum([is_mine(minefield, x,   y+1),
                is_mine(minefield, x+1, y+1),
                is_mine(minefield, x+1, y  ),
                is_mine(minefield, x+1, y-1),
                is_mine(minefield, x,   y-1),
                is_mine(minefield, x-1, y-1),
                is_mine(minefield, x-1, y  ),
                is_mine(minefield, x-1, y+1),])
def annotate(minefield):
    if set(''.join(minefield)) - set(' *'):
        raise ValueError('The board is invalid with current input.')
    if len(set(len(line) for line in minefield)) > 1:
        raise ValueError('The board is invalid with current input.')
    return [''.join('*' if is_mine(minefield, x, y)
                      else str(count_mines(minefield, x, y)).replace('0', ' ')
                    for x in range(len(minefield[y])))
            for y in range(len(minefield))]