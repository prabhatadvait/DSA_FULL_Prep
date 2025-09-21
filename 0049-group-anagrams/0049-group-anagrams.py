from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)  # key: sorted string, value: list of anagrams
        
        for s in strs:
            key = ''.join(sorted(s))  # sort characters and join into a string
            groups[key].append(s)     # append the original string to the corresponding group
        
        return list(groups.values())   # return all grouped anagrams as a list of lists
