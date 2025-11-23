class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # max_len = 0
        # n = len(s)

        # for i in range(n):
        #     x = k
        #     count = 0
        #     freq = [0] * 26
        #     for j in range(i, n):
        #         idx = ord(s[j]) - ord('A')
        #         freq[idx] += 1
        #         most_freq = max(freq)
        #         window_len = j - i + 1
        #         if window_len - most_freq > x:
        #             break
        #         else:
        #             count = window_len
        #     max_len = max(max_len, count)
        # return max_len

        freq = [0]*26
        left = 0
        max_freq = 0
        max_len = 0

        for right in range(len(s)):
            idx = ord(s[right])-ord('A')
            freq[idx] +=1
            max_freq = max(max_freq,freq[idx])

            while (right-left+1)-max_freq>k:
                freq[ord(s[left])- ord('A')] -=1
                left +=1
            max_len = max(max_len,right-left+1)
        return max_len

