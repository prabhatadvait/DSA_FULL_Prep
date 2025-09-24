class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        a = Counter(nums)
        ans = []
        for k,v in a.items():
            if v>(len(nums)/3):
                ans.append(k)
        return ans
