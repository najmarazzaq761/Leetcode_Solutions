class Solution(object):
    def maxDepth(self, s):
        current_depth = 0
        max_depth = 0
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                current_depth = len(stack)
                stack.pop()
            if current_depth > max_depth:
                max_depth = current_depth
        return max_depth
        