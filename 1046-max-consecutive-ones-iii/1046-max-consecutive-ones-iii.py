class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # max_cons = 0
        # for i in range(len(nums)):
        #     x=k
        #     count=0
        #     for j in range(i,len(nums)):
        #         if nums[j]==0 and x<=0:
        #             break
        #         elif nums[j]==0 and x>0:
        #             count=j-i+1
        #             x-=1
        #         else:
        #             count=j-i+1
        #     max_cons = max(max_cons,count)
        # return max_cons

        left=0
        zero_count=0
        max_len=0

        for right in range(len(nums)):
            if nums[right]==0:
                zero_count+=1
            
            while zero_count>k:
                if nums[left]==0:
                    zero_count-=1
                left+=1
            max_len = max(max_len,right-left+1)
        return max_len