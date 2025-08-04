class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(string):
            stack = []
            for char in string:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return "".join(stack)

        return process(s) == process(t)
