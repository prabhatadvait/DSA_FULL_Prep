# from typing import List

# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         if not digits:
#             return []

#         mapping = {
#             "2": "abc",
#             "3": "def",
#             "4": "ghi",
#             "5": "jkl",
#             "6": "mno",
#             "7": "pqrs",
#             "8": "tuv",
#             "9": "wxyz"
#         }

#         ans = []

#         def backtrack(index: int, current: str):
#             if index == len(digits):
#                 ans.append(current)
#                 return

#             for ch in mapping[digits[index]]:
#                 backtrack(index + 1, current + ch)

#         backtrack(0, "")
#         return ans
from typing import List
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # Build the list of letters for each digit
        groups = [mapping[d] for d in digits]

        # Cartesian product of all groups
        return ["".join(p) for p in product(*groups)]
