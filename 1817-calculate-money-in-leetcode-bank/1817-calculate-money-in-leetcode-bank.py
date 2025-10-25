class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        start = 1
        
        for day in range(n):
            total += start + (day % 7)
            if day % 7 == 6:
                start += 1
        return total
