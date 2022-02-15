class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.matrix_list = self.matrix_string.split("\n")
        for index, i in enumerate(self.matrix_list):
            self.matrix_list[index] = list(map(int, i.split()))
    def row(self, index):
        return self.matrix_list[index-1]
        
    def column(self, index):
        return [row[index-1] for row in self.matrix_list]