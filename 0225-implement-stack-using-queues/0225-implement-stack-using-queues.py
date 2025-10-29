from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()   # main queue
        self.q2 = deque()   # helper queue

    def push(self, x: int) -> None:
        # Step 1: Push x into q2
        self.q2.append(x)

        # Step 2: Move all elements from q1 → q2
        while self.q1:
            self.q2.append(self.q1.popleft())

        # Step 3: Swap names (so q1 always has current stack)
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()