class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        from functools import lru_cache

        n = len(nums)
        k=0
        suma = sum(nums)
        if (suma%2)!=0:
            return False
        else:
            k = suma//2
        
        dp = [[-1 for _ in range(k+1)] for _ in range(n)]

        def fun(index,target):
            if target==0:
                return True
            if index==0:
                return nums[0]==target
            if dp[index][target] != -1:
                return dp[index][target]
            nottake = fun(index-1,target)
            take = False
            if nums[index]<target:
                take = fun(index-1,target-nums[index])
            dp[index][target] =  take or nottake
            return dp[index][target]
        return fun(n-1,k)