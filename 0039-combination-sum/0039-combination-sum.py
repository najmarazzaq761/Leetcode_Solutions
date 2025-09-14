from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current, total):
            # base case: found a valid combination
            if total == target:
                result.append(list(current))
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, total + candidates[i])  # not i+1 because we can reuse same number
                current.pop()  # backtrack

        backtrack(0, [], 0)
        return result
