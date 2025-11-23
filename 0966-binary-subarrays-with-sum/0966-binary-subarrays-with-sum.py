class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # count=0
        # n = len(nums)
        # for i in range(n):
        #     suma=0
        #     for j in range(i,n):
        #         suma += nums[j]
        #         if suma == goal:
        #             count+=1
        #         if suma>goal:
        #             break
        # return count

        def fun(nums,k):
            if k<0:
                return 0
            left = 0
            curr_sum=0
            count=0

            for right in range(len(nums)):
                curr_sum += nums[right]

                while curr_sum>k:
                    curr_sum -= nums[left]
                    left+=1
                count += (right-left+1)
            return count
        return fun(nums,goal)-fun(nums,goal-1)