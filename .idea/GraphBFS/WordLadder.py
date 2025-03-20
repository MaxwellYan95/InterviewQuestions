class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0;
        if len(wordList) == 1:
            if endWord == wordList[0]:
                return 1;
            return 0;
        numbers = [];
        for word in wordList:
            if self.canTransform(beginWord, word) == True:
                if word == endWord:
                    numbers.append(1);
                lst = wordList;
                lst.remove(word);
                prevMoves = self.ladderLength(word, endWord, lst);
                if prevMoves != 0:
                    numbers.append(1 + prevMoves);
        if len(numbers) == 0:
            return 0;
        return min(numbers);

    def canTransform(self, first: str, second: str):
        firstList = list(first);
        secondList = list(second);
        changes = 0;
        for index in range(len(firstList)):
            if firstList[index] != secondList[index]:
                changes = changes + 1;
        return changes < 2;

sol = Solution();
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]));
