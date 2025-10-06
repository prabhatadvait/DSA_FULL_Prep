class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows,cols = len(matrix),len(matrix[0])
        row = 0
        col = cols-1
        while row<rows and col >=0:
            current_val = matrix[row][col]
            if current_val==target:
                return True
            elif target<=current_val:
                col-=1
            else:
                row+=1
        return False