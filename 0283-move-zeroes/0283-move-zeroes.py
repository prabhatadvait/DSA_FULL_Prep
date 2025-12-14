class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # numZeros = 0
        # for i in nums:
        #     if i==0:
        #         numZeros += 1
        # ans = []
        # for i in nums:
        #     if i!= 0:
        #         ans.append(i)
        # while numZeros:
        #     ans.append(0)
        #     numZeros-=1
        # for i in range(len(ans)):
        #     nums[i]=ans[i]
        # return nums
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
        