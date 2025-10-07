class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        peri = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    peri += 4

                    if row > 0 and grid[row - 1][col] == 1:
                        peri -= 2
                        
                    if col > 0 and grid[row][col - 1] == 1:
                        peri -= 2                     
        return peri
