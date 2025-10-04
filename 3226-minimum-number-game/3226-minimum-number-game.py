class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans = []
        while nums:
            alice = min(nums)
            nums.remove(alice)
            bob = min(nums)
            nums.remove(bob)
            
            ans.append(bob)
            ans.append(alice)
        return ans
