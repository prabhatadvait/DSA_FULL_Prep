class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute Force
        # max_len = 0
        # for i in range(len(s)):
        #     visited_char = ""
        #     for j in range(i,len(s)):
        #         if s[j] in visited_char:
        #             break
        #         lent = j-i+1
        #         max_len = max(max_len,lent)
        #         visited_char += s[j]
        # return max_len

        left=0
        seen = set()
        max_len=0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            
            seen.add(s[right])
            max_len = max(max_len,right-left+1)
        return max_len