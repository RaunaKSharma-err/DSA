class solution:
    def spiralMatrix(self, matrix):
        result = []
        i = j = 0
        while i < len(matrix):
            result.append(matrix[i][j])
            if j < len(matrix[0]) - 1:
                j += 1
            else:
                i += 1

        print(result)


m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
c = solution()
c.spiralMatrix(m)
