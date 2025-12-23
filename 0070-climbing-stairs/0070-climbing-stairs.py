class Solution:
    def climbStairs(self, n: int) -> int:
        # first = 1
        # second = 2
        # if n <= 2:
        #     return n
        # for i in range(3, n+1):
        #     third = first + second
        #     first, second = second, third
        # return second
        if n < 0:
            return 0
        if n == 1:
            return 1
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]