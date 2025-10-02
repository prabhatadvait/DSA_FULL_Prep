class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[-k]

        import heapq
        heapq.heapify(nums)
        return heapq.nlargest(k,nums)[-1]