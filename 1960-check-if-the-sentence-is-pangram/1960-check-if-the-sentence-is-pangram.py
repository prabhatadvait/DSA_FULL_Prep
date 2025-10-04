class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        from collections import Counter
        a = Counter(sentence)
        if len(a)==26:
            return True
        return False