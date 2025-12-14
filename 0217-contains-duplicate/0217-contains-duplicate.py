class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        freq = Counter(nums)
        for i in freq.values():
            if i > 1:
                return True
        return False