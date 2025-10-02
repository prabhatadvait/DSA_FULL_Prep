from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        total_len = 0
        
        for word in words:
            word_count = Counter(word)
            if all(word_count[c] <= char_count[c] for c in word_count):
                total_len += len(word)
        return total_len
