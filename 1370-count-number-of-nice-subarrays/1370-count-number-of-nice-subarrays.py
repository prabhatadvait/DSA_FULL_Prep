class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # ans=0
        # for i in range(n):
        #     count=0
        #     for j in range(i,n):
        #         if nums[j]%2!=0:
        #             count+=1
        #         if count==k:
        #             ans+=1
        #         elif count>k:
        #             break
        # return ans

        def fun(nums,k):
            if k<0:
                return 0
            left=0
            curr_sum=0
            count=0

            for right in range(len(nums)):
                curr_sum += nums[right]

                while curr_sum >k:
                    curr_sum -= nums[left]
                    left +=1
                count += right-left+1
            return count
        binary = [0 if n%2 ==0 else 1 for n in nums]
        return fun(binary,k)-fun(binary,k-1)
