
OCR = {
    (' _ ', '| |', '|_|', '   '): "0",
    ('   ', '  |', '  |', '   '): "1",
    (' _ ', ' _|', '|_ ', '   '): "2",
    (' _ ', ' _|', ' _|', '   '): "3",
    ('   ', '|_|', '  |', '   '): "4",
    (' _ ', '|_ ', ' _|', '   '): "5",
    (' _ ', '|_ ', '|_|', '   '): "6",
    (' _ ', '  |', '  |', '   '): "7",
    (' _ ', '|_|', '|_|', '   '): "8",
    (' _ ', '|_|', ' _|', '   '): "9",
}
def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError('Number of input lines is not a multiple of four')
    if any(len(r) % 3 for r in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")
    rows = []
    for i in range(0, len(input_grid), 4):
        digit_str = []
        for k in range(0, len(input_grid[0]), 3):
            digit = []
            for j in range(0, 4):
                digit.append(input_grid[i+j][k:k+3])
            digit_str.extend(digit)
        rows.append(tuple(digit_str))
    return decode_digits(rows)
def decode_digits(rows):
    digits = []
    for row in rows:
        digit_row = ''
        for i in range(0, len(row), 4):
            digit_row += OCR.get(row[i:i+4], "?")
        digits.append(digit_row)
    return ",".join(digits)
