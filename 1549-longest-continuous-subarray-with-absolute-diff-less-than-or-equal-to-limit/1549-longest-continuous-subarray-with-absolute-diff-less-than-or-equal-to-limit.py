# 1. Brute Force Approach
# class Solution:
#     def longestSubarray(self, nums: List[int], limit: int) -> int:
#         n = len(nums)
#         max_len = 0
        
#         for i in range(n):
#             curr_max, curr_min = nums[i], nums[i]
#             for j in range(i, n):
#                 curr_max = max(curr_max, nums[j])
#                 curr_min = min(curr_min, nums[j])
                
#                 if curr_max - curr_min <= limit:
#                     max_len = max(max_len, j - i + 1)
#                 else:
#                     # since nums[j] only increases window, no need to continue
#                     break
        
#         return max_len

class Solution:
    def longestSubarray(self,nums,limit):
        from collections import deque
        max_d, min_d = deque(), deque()
        left = 0
        res =  0 

        for right, num in enumerate(nums):

            while max_d and num > max_d[-1]:
                max_d.pop()
            max_d.append(num)

            while min_d and num < min_d[-1]:
                min_d.pop()
            min_d.append(num)

            ##shrink window if invalid
            
            while max_d[0] - min_d[0] > limit:
                if nums[left] == max_d[0]:
                    max_d.popleft()
                if nums[left] == min_d[0]:
                    min_d.popleft()
                left+=1
            res = max(res,right-left+1)
        return res
