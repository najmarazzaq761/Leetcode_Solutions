class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)
            elif t == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif t == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
            elif t == "/":
                a = stack.pop()
                b = stack.pop()
                if a > 0 and b < 0 or a < 0 and b > 0:
                    stack.append(-(abs(b) // abs(a)))
                else:
                    stack.append(abs(b) // abs(a))
            else:
                stack.append(int(t))
        return stack[0]
        