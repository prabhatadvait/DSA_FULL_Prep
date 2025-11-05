class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # sum1=sum2=0
        # zeros1=zeros2=0

        # for i in nums1:
        #     if i==0:
        #         sum1+=1
        #         zeros1+=1
        #     else:
        #         sum1+=i
        
        # for i in nums2:
        #     if i==0:
        #         sum2+=1
        #         zeros2+=1
        #     else:
        #         sum2+=i
        # if (zeros1 == 0 and sum2>sum1) or (zeros2 == 0 and sum1 > sum2):
        #     return -1
        # return max(sum1,sum2)

        sum1 = sum(nums1)+nums1.count(0)
        sum2 = sum(nums2)+nums2.count(0)
        zeros1= nums1.count(0)
        zeros2 = nums2.count(0)

        if (zeros1 ==0 and sum2>sum1) or (zeros2 == 0 and sum1>sum2):
            return -1
        return max(sum1,sum2)
        
