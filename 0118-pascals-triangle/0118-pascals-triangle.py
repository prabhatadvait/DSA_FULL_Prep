class Solution:
    def generateRow(self, row: int):
        ans = 1
        ansRow = [1]

        for col in range(1, row):
            ans = ans * (row - col)
            ans = ans // col  # integer division
            ansRow.append(ans)

        return ansRow

    def generate(self, numRows: int) -> list[list[int]]:
        res = []
        for i in range(1, numRows + 1):
            res.append(self.generateRow(i))
        return res
