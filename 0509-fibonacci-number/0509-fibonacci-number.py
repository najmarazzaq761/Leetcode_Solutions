class Solution:
    def fib(self, n: int) -> int:
        # if n==0 or n==1:
        #     return n
        # return self.fib(n-1) + self.fib(n-2)
        if n<=1:
            return n
        a = 0
        b = 1

        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return c
