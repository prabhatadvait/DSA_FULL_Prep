class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele_s = sum(nums)
        digit_s=0
        for i in nums:
            if i <10:
                digit_s+=i
            else:
                while i>0:
                    rem = i%10
                    digit_s+=rem
                    i=i//10
        return abs(ele_s-digit_s)