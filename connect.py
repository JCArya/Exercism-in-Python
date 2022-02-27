DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (1, -1), (0, 1), (-1, 1)]
class ConnectGame:
    """Connect game logic.
 
    The board internally stores the fields as a rectangle (2d array).
    The parallelogram shape is emulated via `self.adjacent` function that
    correctly resolves all the field's neighbor under this transformation.
    """
    def __init__(self, board):
        self.board = [[c for c in row if not c.isspace()] for row in board.splitlines()]
        self.width = len(self.board[0])
        self.height = len(self.board)
    def value(self, x: int, y: int) -> str:
        """Returns the value of the given field."""
        return self.board[y][x]
    def adjacent(self, x: int, y: int, player: str) -> list[tuple[int, int]]:
        """Returns all adjacent fields with stones of the given player."""
        is_valid = lambda x, y: self.in_range(x, y) and self.value(x, y) == player
        return [f for (dx, dy) in DIRECTIONS if is_valid(*(f := (x + dx, y + dy)))]
    def in_range(self, x: int, y: int) -> bool:
        """Checks if the coordinates are within the board."""
        return 0 <= x < self.width and 0 <= y < self.height
    def top(self):
        """Returns the coordinates of the top row."""
        return list((x, 0) for x in range(self.width))
    def left(self):
        """Returns the coordinates of the left-most column."""
        return list((0, y) for y in range(self.height))
    def is_bottom(self, _, y):
        """Checks if the coordinates are in the bottom row."""
        return y == self.height - 1
    def is_right(self, x, _):
        """Checks if the coordinates are in the right-most column."""
        return x == self.width - 1
    def get_winner(self):
        """Finds the winner."""
        if self.check_winner("O", start=self.top(), end_condition=self.is_bottom):
            return "O"
        if self.check_winner("X", start=self.left(), end_condition=self.is_right):
            return "X"
        return ""
    def check_winner(self, player, start: list[tuple[int, int]], end_condition) -> bool:
        """Checks if the given player is the winner.
 
        It traverses the neighbor graph starting from the given set of fields
        until it reaches the end condition (`player` wins) or traverses all
        connected components originating from the start positions.
        """
        visited = set()
        for start_field in start:
            if self.value(*start_field) != player or start_field in visited:
                continue
            queue = [start_field]
            visited.add(start_field)
            while queue:
                field = queue.pop(0)
                if end_condition(*field):
                    return True
                for adj in self.adjacent(*field, player):
                    if adj not in visited:
                        queue.append(adj)
                        visited.add(adj)
        return False