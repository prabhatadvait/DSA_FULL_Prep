class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        def is_increasing(sub):
            return all(sub[i] < sub[i+1] for i in range(len(sub)-1))

        for i in range(0, n - 2*k + 1):
            first = nums[i:i+k]
            second = nums[i+k:i+2*k]
            if is_increasing(first) and is_increasing(second):
                return True
        return False