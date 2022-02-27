ROW, COLUMN = ("row", "column")

        

          


        

          


        

          

def valid_matrix(matrix):

        

          

    return len(set(map(len, matrix))) <= 1

        

          


        

          


        

          

def saddle_points(matrix):

        

          

    if not valid_matrix(matrix):

        

          

        raise ValueError("irregular matrix")

        

          


        

          

    result = []

        

          


        

          

    for i, row in enumerate(matrix):

        

          

        max_value = max(row)

        

          

        for j, value in enumerate(row):

        

          

            if value == max_value == min(r[j] for r in matrix):

        

          

                result.append({ROW: i + 1, COLUMN: j + 1})

        

          


        

          

    return result