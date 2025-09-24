from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize max_product, min_product, result
        max_prod = min_prod = result = nums[0]
        
        for num in nums[1:]:
            if num < 0:
                # Swap max and min because negative flips signs
                max_prod, min_prod = min_prod, max_prod
            
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)
            
            result = max(result, max_prod)
        
        return result