from typing import List
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        # If grid is too small to trap water
        if m < 3 or n < 3:
            return 0

        visited = [[False] * n for _ in range(m)]
        heap: List[tuple[int, int, int]] = []  # (height, r, c)

        # Push all border cells into heap and mark visited
        for r in range(m):
            for c in (0, n - 1):
                heapq.heappush(heap, (heightMap[r][c], r, c))
                visited[r][c] = True
        for c in range(n):
            for r in (0, m - 1):
                if not visited[r][c]:
                    heapq.heappush(heap, (heightMap[r][c], r, c))
                    visited[r][c] = True

        water = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while heap:
            height, r, c = heapq.heappop(heap)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    neigh_h = heightMap[nr][nc]
                    # If neighbor is lower than current boundary, water is trapped
                    if neigh_h < height:
                        water += height - neigh_h
                        # neighbor effective height becomes height (water fills up to boundary)
                        heapq.heappush(heap, (height, nr, nc))
                    else:
                        # neighbor is higher or equal: becomes a new boundary
                        heapq.heappush(heap, (neigh_h, nr, nc))

        return water
