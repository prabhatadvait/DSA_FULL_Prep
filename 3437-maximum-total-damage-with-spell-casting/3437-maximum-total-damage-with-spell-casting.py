class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        from collections import Counter
        from functools import lru_cache

        count = Counter(power)
        unique = sorted(count.keys())
        n = len(unique)

        @lru_cache(None)
        def fun(i):
            if i>=n:
                return 0
            take_dam = count[unique[i]] * unique[i]
            next_i = i+1
            while next_i < n and unique[next_i] <= unique[i]+2:
                next_i += 1
            take = take_dam  + fun(next_i)
            not_take = fun(i+1)
            return max(take,not_take)
        return fun(0)