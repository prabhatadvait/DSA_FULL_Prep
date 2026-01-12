from functools import lru_cache
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        n = len(stones)

        @lru_cache(maxsize=None)
        def fun(index, curr_sum):
            if curr_sum > target:
                return 0

            if index == n:
                return curr_sum

            not_take = fun(index + 1, curr_sum)
            take = fun(index + 1, curr_sum + stones[index])

            return max(take, not_take)

        best = fun(0, 0)
        return total - 2 * best
