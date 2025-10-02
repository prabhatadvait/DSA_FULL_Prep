class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # Step 2: Min-heap of size k
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))   # push (frequency, number)
            if len(heap) > k:
                heapq.heappop(heap)             # remove smallest frequency

        # Step 3: extract only numbers from heap
        return [num for count, num in heap]