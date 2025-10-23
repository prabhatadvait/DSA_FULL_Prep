class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n=len(s)
        digit = [int(ch) for ch in s]
        for i in range(1,n-1):
            for j in range(n-i):
                d1 = digit[j]
                d2 = digit[j+1]
                digit[j] = (d1+d2)%10
        return digit[0]==digit[1]
