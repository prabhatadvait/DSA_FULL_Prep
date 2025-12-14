class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        freq = Counter(nums)
        for key,val in freq.items():
            if val!=2:
                return key
        return None