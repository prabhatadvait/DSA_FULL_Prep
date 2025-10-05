class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        a = num
        while a > 0:
            val = a % 10
            if val != 0 and num % val == 0:
                count += 1
            a = a // 10
        return count