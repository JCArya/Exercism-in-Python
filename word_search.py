
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle
    def search(self, word):
        #       right    left     down     up      diags...
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1))
        def valid(x, y):
            return 0 <= x < len(self.puzzle[0]) and 0 <= y < len(self.puzzle)
        def get_char(x, y):
            return self.puzzle[x][y]
        for i, row in enumerate(self.puzzle):
            for idx, c in enumerate(row):
                # Just try different directions when first letter matches
                if c != word[0]:
                    continue
                for mdir in dirs:
                    point = (idx, i)
                    found = True
                    for c in word[1:]:
                        point = (point[0] + mdir[0], point[1] + mdir[1])
                        if not valid(*point) or get_char(*point[::-1]) != c:
                            found = False
                            break
                    if found:
                        return Point(idx, i), Point(*point)
        return None
