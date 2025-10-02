from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # char_count = Counter(chars)
        # total_len = 0
        
        # for word in words:
        #     word_count = Counter(word)
        #     if all(word_count[c] <= char_count[c] for c in word_count):
        #         total_len += len(word)
        # return total_len


        char_count = [0] * 26
        for ch in chars:
            char_count[ord(ch) - ord('a')] += 1
        
        total_len = 0
        for word in words:
            word_count = [0] * 26
            for ch in word:
                word_count[ord(ch) - ord('a')] += 1
                
            valid = True
            for i in range(26):
                if word_count[i] > char_count[i]:
                    valid = False
                    break
            
            if valid:
                total_len += len(word)
        
        return total_len