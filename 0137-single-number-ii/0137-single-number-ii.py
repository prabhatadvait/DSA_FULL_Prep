class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # from collections import Counter
        # d = Counter(nums)

        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1
        for i,j in d.items():
            if j<3:
                return i