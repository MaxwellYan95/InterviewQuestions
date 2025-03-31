class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s);
        dp = [False] * (n+1);
        dp[0] = True;
        maxLen = max([len(i) for i in wordDict]);
        minLen = min([len(i) for i in wordDict]);
        for i in range(1, n+1):
            for j in range(0, i):
                if s[j: i] in wordDict and dp[j] == True:
                    dp[i] = True;
        return dp[n];


sol = Solution();
sol.wordBreak("leetcode", ["leet", "code"]);

