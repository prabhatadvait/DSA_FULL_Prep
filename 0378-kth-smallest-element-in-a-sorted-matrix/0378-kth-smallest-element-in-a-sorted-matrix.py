import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for row in matrix:
            for val in row:
                heapq.heappush(heap, -val)  # push negative for max-heap
                if len(heap) > k:
                    heapq.heappop(heap)     # pop the largest (most negative = smallest in original)
        return -heap[0]  # kth smallest
