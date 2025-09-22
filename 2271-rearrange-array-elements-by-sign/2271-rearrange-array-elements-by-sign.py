class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # neg_id = []
        # pos_id = []
        # for i in nums:
        #     if i<0:
        #         neg_id.append(i)
        #     else:
        #         pos_id.append(i)
        # m,j=0,0
        # while j<len(pos_id):
        #     nums[m] = pos_id[j]
        #     m+=2
        #     j+=1
        # k=1
        # i=0
        # while i<len(neg_id):
        #     nums[k]=neg_id[i]
        #     k+=2
        #     i+=1 
        # return nums
        n = len(nums)
        ans = [0] * n   # pre-allocate space
        pos_idx, neg_idx = 0, 1

        for num in nums:
            if num < 0:
                ans[neg_idx] = num
                neg_idx += 2
            else:
                ans[pos_idx] = num
                pos_idx += 2

        return ans
