class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        rows = [0] * row
        cols = [0] * col

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    rows[r] = 1
                    cols[c] = 1

        for i in range(row):
            for j in range(col):
                if rows[i] == 1 or cols[j] == 1:
                    matrix[i][j] = 0
