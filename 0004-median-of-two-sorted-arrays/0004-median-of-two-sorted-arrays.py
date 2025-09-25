class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1+nums2
        lent = len(merged)
        merged.sort()
        ans=0
        if(lent)%2==0:
            ans = (merged[(lent)//2]+merged[((lent)//2)-1])/2
        else:
            ans = merged[(lent)//2]
        return ans