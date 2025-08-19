class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            for word in word_set:
                if i>=len(word) and dp[i-len(word)] and s[i-len(word):i] == word:
                    dp[i] = True
                    break
        return dp[n]