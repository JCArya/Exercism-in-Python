
class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        if 7 < row:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if 7 < column:
            raise ValueError("column not on board")
        self.row = row
        self.column = column
    def can_attack(self, another_queen):
        row_offset = abs(self.row - another_queen.row)
        column_offset = abs(self.column - another_queen.column)
        same_row = row_offset == 0
        same_column = column_offset == 0
        if same_row and same_column:
            raise ValueError(
                "Invalid queen position: both queens in the same square")
        same_diagonal = row_offset == column_offset
        return same_row or same_column or same_diagonal