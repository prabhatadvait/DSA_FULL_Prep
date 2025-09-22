class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        a = Counter(nums)
        n=len(nums)
        for key,value in a.items():
            if value > n//2:
                return key