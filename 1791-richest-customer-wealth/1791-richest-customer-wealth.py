class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth=0
        for num in accounts:
            wealth = sum(num)
            max_wealth = max(max_wealth,wealth)
        return max_wealth