WHITE, BLACK, NONE = 'W', 'B', ''
class Board:
    """Count territories of each player in a Go game
 
    Args:
        board (list[str]): A two-dimensional Go board
    """
    def __init__(self, board):
        def find_all_territories(player, opponent):
            if player in "".join(board):
                board_filled = self._fill_squares(opponent)
                return {(y, x) for x in range(len(board)) for y in range(len(board[0])) if board_filled[x][y] == ' '}
            return set()
        
        self.board = board
        self.territory_dict = {BLACK: find_all_territories(BLACK, WHITE), 
                               WHITE: find_all_territories(WHITE, BLACK)}
        no_stones = {(y, x) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == ' '}
        self.territory_dict[NONE] = no_stones - self.territory_dict[BLACK] - self.territory_dict[WHITE]
    def _fill_squares(self, fill_with, start_fill = None):
        def surroundings(x, y):
            adjacent_coords = [(i + x, j + y) for i in range(-1, 2) for j in range(-1, 2) if abs(i) != abs(j)]
            return [coords for coords in adjacent_coords if 0 <= coords[0] < len(self.board[0]) and 0 <= coords[1] < len(self.board)]
            
        board = self.board.copy()
        if start_fill != None:
            x, y = start_fill
            board[x] = board[x][:y] + fill_with + board[x][y + 1:]
        prev_board = None
        while prev_board != board:
            prev_board = board.copy()
            for y in range(len(self.board)):
                for x in range(len(self.board[0])):
                    if board[y][x] == fill_with:
                        for i, j in surroundings(x, y):
                            if board[j][i] == ' ':
                                board[j] = board[j][:i] + fill_with + board[j][i + 1:]
        return board
    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board
 
        Args:
            x (int): Column on the board
            y (int): Row on the board
 
        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        if 0 <= x < len(self.board[0]) and 0 <= y < len(self.board):
            if self.board[x][y] != ' ':
                return (NONE, set())
            board = self._fill_squares('*', (x, y))
            for k, v in self.territory_dict.items():
                if (x, y) in v:
                    return (k, {(j, i) for i in range(len(self.board)) for j in range(len(self.board[0])) if board[j][i] == '*'})
            return (NONE, {(j, i) for i in range(len(self.board)) for j in range(len(self.board[0])) if board[j][i] == '*'})
        else:
            raise ValueError("Invalid coordinate")
    def territories(self):
        """Find the owners and the territories of the whole board
 
        Args:
            none
 
        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        return self.territory_dict
