class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        # from functools import lru_cache
        # @lru_cache(None)
        # def fun(index,prev_ind):
        #     if index>=n:
        #         return 0
        #     lent = 0+fun(index+1,prev_ind)
        #     if(prev_ind==-1 or nums[prev_ind]<nums[index]):
        #         lent = max(lent,1+fun(index+1,index))
        #     return lent
        # return fun(0,-1)
        dp = [1] * n  # Initialize dp with 1 because the smallest LIS ending at each element is 1
        for index in range(n):
            for prev_ind in range(index):
                if nums[prev_ind] < nums[index]:  # valid increasing sequence
                    dp[index] = max(dp[index], 1 + dp[prev_ind])
        return max(dp)