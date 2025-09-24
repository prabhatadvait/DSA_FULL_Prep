class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        #prefix sum approach
        prefix_count = {0:1}
        presum=0
        count=0

        for num in nums:
            presum += num
            remove = presum-k

            count += prefix_count.get(remove,0)
            prefix_count[presum] = prefix_count.get(presum,0)+1
        return count