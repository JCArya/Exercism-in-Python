
from itertools import zip_longest
def transpose(lines):
    """Given a string return its transpose.
 
    Keep padding on the left, but remove padding on the right
    """
    # ABC\n123 -> ['ABC', '123']
    lines = lines.split('\n')
    transpose_lines = []
    # Necessary to use a fill different from ' ', @ is easy to see.
    for row in zip_longest(*lines, fillvalue='@'):
        row_str = ''.join(row)
        row_str = row_str.rstrip('@').replace('@', ' ')
        transpose_lines.append(row_str)
    return '\n'.join(transpose_lines)
