class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # from collections import Counter
        # a = Counter(nums)
        # n=len(nums)
        # for key,value in a.items():
        #     if value > n//2:
        #         return key

        my_dict = {}
        for i in nums:
            my_dict[i] = my_dict.get(i,0)+1
        n = len(nums)
        for key,value in my_dict.items():
            if value > n//2:
                return key