class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0

        for i in range(len(s)):
            check_str = ""
            for j in range(i,len(s)):
                if s[j] in check_str:
                    break
                lent = j-i+1
                maxlen = max(maxlen,lent)
                check_str+=s[j]
        return maxlen