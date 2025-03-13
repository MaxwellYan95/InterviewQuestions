class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        sortedWord = sorted(wordDict, key=len, reverse=True);
        if len(sortedWord[len(sortedWord)-1]) < len(s):
            return False;
        if len(s) == 0:
            return True;
        for word in sortedWord:
            isLength = (len(word) <= len(s));
            if s[0: len(word)] == word and isLength:
                iter = self.wordBreak(s[len(word):], wordDict);
                if iter == True:
                    return True;
        return False;

sol = Solution();
sol.wordBreak("leetcode", ["leet", "co"]);

