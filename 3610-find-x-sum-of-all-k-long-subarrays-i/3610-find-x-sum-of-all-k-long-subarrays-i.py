class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        
        def xsum(nums,k):
            from collections import Counter
            freq = Counter(nums)
            heap = []
            for key,val in freq.items():
                heapq.heappush(heap,(val,key))
                if len(heap) > k:
                    heapq.heappop(heap)
            total=0
            for _ in range(len(heap)):
                k,v = heapq.heappop(heap)
                total += k*v
            return total
        for i in range(len(nums)-k+1):
                ans.append(xsum(nums[i:k+i],x))
        return ans