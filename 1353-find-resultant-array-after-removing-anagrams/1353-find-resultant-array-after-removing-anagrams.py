class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # result = [words[0]]
        # for i in range(1,len(words)):
        #     if Counter(words[i])!=Counter(words[i-1]):
        #         result.append(words[i])
        # return result

        res = []
        prev_sorted = ""
        for word in words:
            sorted_word = ''.join(sorted(word))
            if sorted_word != prev_sorted:
                res.append(word)
                prev_sorted = sorted_word
        return res
