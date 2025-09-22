class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg_id = []
        pos_id = []
        for i in nums:
            if i<0:
                neg_id.append(i)
            else:
                pos_id.append(i)
        m,j=0,0
        while j<len(pos_id):
            nums[m] = pos_id[j]
            m+=2
            j+=1
        k=1
        i=0
        while i<len(neg_id):
            nums[k]=neg_id[i]
            k+=2
            i+=1 
        return nums