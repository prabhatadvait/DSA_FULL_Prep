class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (n+1)
        result = []
        
        for i in nums:
            ans[i]+=1

        for i in range(1,n+1):
            if ans[i]==0:
                result.append(i)
        return result
            
        # freq = {}
        # n = len(nums)
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1
        
        # result = []
        # for i in range(1, n + 1):
        #     if i not in freq:
        #         result.append(i)
        
        # return result
