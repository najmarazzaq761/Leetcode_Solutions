class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []

        def backtrack(current : str, open_used: int, closed_used: int):

            # base case : all brackets used
            if len(current) == 2*n:
                result.append(current)
                return
            # try adding an opening bracket
            if open_used < n:
                backtrack(current + "(", open_used + 1, closed_used)
            
            # try adding an opening bracket only if it wont break validity
            if closed_used < open_used:
                backtrack( current + ")", open_used, closed_used + 1)

        # start recursion 
        backtrack("", 0, 0)
        return result
