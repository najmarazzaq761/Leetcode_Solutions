class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []
        path = []

        def backtrack(i: int):
            if i == len(digits):
                res.append("".join(path))
                return

            for ch in phone[digits[i]]:
                path.append(ch)        # choose
                backtrack(i + 1)       # explore
                path.pop()             # un-choose (backtrack)

        backtrack(0)
        return res
