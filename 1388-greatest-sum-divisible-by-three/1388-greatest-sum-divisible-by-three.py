class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        from functools import lru_cache
        
        n = len(nums)

        @lru_cache(None)
        def solve(i, rem):
            if i == n:
                return 0 if rem == 0 else float('-inf')
            skip = solve(i + 1, rem)
            new_rem = (rem + nums[i]) % 3
            take = nums[i] + solve(i + 1, new_rem)
            return max(skip, take)
        ans = solve(0, 0)
        return ans if ans != float('-inf') else 0