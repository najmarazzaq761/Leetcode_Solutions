class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        new_list = [0] * len(T)

        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                index = stack.pop()
                new_list [index] = i-index

            stack.append(i)
        return new_list 