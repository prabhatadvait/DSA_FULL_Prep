class Solution:
    def addDigits(self, num: int) -> int:
        if num <10:
            return num
        while num >= 10:
            a = num//10
            b = num%10
            num=a+b
        return num