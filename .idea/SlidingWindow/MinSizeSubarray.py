class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tList = list(t);
        minLen = len(s);
        indexDict, indexList = self.indexDictAndList(s, t);
        minWin = "";



    def indexDictAndList(self, s: str, t: str) -> (dict, list[int]):
        indexDict = {};
        indexList = [];
        for letter in set(list(t)):
            indexes = self.allOccurences(s, letter);
            for ind in indexes:
                indexDict[ind] = letter;
                indexList.append(ind);
        indexList.sort();
        return (indexDict, indexList);

    def allOccurences(self, s: str, letter: str) -> list[int]:
        startInd = 0;
        endInd = len(s);
        indexes = [];
        while True:
            if startInd >= len(s):
                break;
            if letter not in s[startInd: endInd]:
                break;
            ind = s.index(letter, startInd, endInd);
            indexes.append(ind);
            startInd = ind+1;
        return indexes;



sol = Solution();
print(sol.minWindow("ADOBECODEBANC", "ABC"));
