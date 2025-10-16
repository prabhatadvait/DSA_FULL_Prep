class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        org =x
        ans=0
        rem =0
        while x!=0:
            rem = x%10
            ans = ans*10 + rem
            x = x//10
        return ans == org