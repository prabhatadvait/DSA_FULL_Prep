class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # ans=0
        # n = len(s)
        # chr = ["a","b","c"]
        # for i in range(n):
        #     cha = ""
        #     count=0
        #     for j in range(i,n):
        #         if s[j] in chr and s[j] not in cha:
        #             cha += s[j]
        #             count+=1
        #         if count==3:
        #             ans+=1
        # return ans
        
        count = {'a':0, 'b':0,'c':0}
        left  = 0
        result = 0

        for right in range(len(s)):

            count[s[right]]+=1

            while count['a']>0 and count['b'] >0 and count['c']>0:
                result+= len(s)-right
                count[s[left]]-=1
                left+=1
        return result
