from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        if len(nums) < 3:
            return res
        
        # Sort the array
        nums.sort()
        
        # Use a set to avoid duplicates
        result_set = set()
        
        # Fix the first element and use two pointers
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                
                if s == 0:
                    # convert to tuple since set requires hashable elements
                    result_set.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        
        # Convert set of tuples back to list of lists
        res = [list(triplet) for triplet in result_set]
        return res
