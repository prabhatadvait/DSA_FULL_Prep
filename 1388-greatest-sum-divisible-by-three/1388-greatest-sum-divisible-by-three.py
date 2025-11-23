class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, None, None] 

        for num in nums:
            prev = dp[:]
            for r in range(3):
                if prev[r] is not None:
                    cand = prev[r] + num
                    rem = cand % 3
                    if dp[rem] is None:
                        dp[rem] = cand
                    else:
                        dp[rem] = max(dp[rem], cand)
        return dp[0] if dp[0] is not None else 0