class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        from collections import Counter

        ans = []
        count = Counter(nums)
        for key,val in count.items():
            if val==2:
                ans.append(key)
        return ans
    