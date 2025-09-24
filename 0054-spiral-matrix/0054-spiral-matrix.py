class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        left, right = 0, col - 1
        top, bottom = 0, row - 1
        
        ans = []

        while left <= right and top <= bottom:
            # Top row
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            # Right column
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # Bottom row (if not already traversed)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            # Left column (if not already traversed)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans
