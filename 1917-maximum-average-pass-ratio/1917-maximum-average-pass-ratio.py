from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # build max-heap by pushing (-delta, p, t) where delta = (p+1)/(t+1) - p/t
        heap = []
        for p, t in classes:
            delta = (p + 1) / (t + 1) - p / t
            heapq.heappush(heap, (-delta, p, t))

        # assign each extra student greedily to the class with largest marginal gain
        for _ in range(extraStudents):
            neg_delta, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            new_delta = (p + 1) / (t + 1) - p / t
            heapq.heappush(heap, (-new_delta, p, t))

        # compute final average pass ratio
        total = 0.0
        for _, p, t in heap:
            total += p / t
        return total / len(classes)