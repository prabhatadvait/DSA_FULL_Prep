class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        low = grid[0][0]
        high = n * n - 1
        min_working_time = high

        while low <= high:
            mid = low + (high - low) // 2
            
            if can_reach_end_with_bfs(grid, mid):
                min_working_time = mid
                high = mid - 1
            else:
                low = mid + 1
            
        return min_working_time


def can_reach_end_with_bfs(grid: list[list[int]], time_limit: int) -> bool:
    n = len(grid)
    
    if grid[0][0] > time_limit:
        return False

    queue = collections.deque([(0, 0)])
    visited = {(0, 0)}

    while queue:
        row, col = queue.popleft()

        if row == n - 1 and col == n - 1:
            return True

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc

            if (0 <= new_row < n and 0 <= new_col < n and
                (new_row, new_col) not in visited and
                grid[new_row][new_col] <= time_limit):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col))
    
    return False