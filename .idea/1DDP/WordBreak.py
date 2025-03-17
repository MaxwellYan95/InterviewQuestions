class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        sortedWord = sorted(wordDict, key=len);
        if len(s) == 0:
            return True;
        if len(sortedWord[0]) > len(s):
            return False;
        for word in sortedWord:
            isLength = (len(word) <= len(s));
            if s[0: len(word)] == word and isLength:
                iter = self.wordBreak(s[len(word):], wordDict);
                if iter == True:
                    return True;
        return False;

sol = Solution();
sol.wordBreak("leetcode", ["leet", "code"]);

