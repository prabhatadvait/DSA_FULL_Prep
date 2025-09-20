class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}   # prefix_sum -> first index
        ## here d :-> sum,index
        count = 0
        max_len = 0

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in d:
                max_len = max(max_len, i - d[count])
            else:
                d[count] = i
        return max_len