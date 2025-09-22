class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        n = len(s)
        # Initialize 2D grid with empty strings
        grid = [[""] * n for _ in range(numRows)]

        row, col = 0, 0
        direction_down = True  # Start moving downward

        for ch in s:
            grid[row][col] = ch

            if direction_down:
                if row == numRows - 1:  # hit bottom, switch
                    direction_down = False
                    row -= 1
                    col += 1
                else:
                    row += 1
            else:
                if row == 0:  # hit top, switch
                    direction_down = True
                    row += 1
                else:
                    row -= 1
                    col += 1

        # Collect result row by row
        result = []
        for r in grid:
            result.append("".join([c for c in r if c != ""]))
        return "".join(result)
