class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            visited_char = ""
            for j in range(i,len(s)):
                if s[j] in visited_char:
                    break
                lent = j-i+1
                max_len = max(max_len,lent)
                visited_char += s[j]
        return max_len