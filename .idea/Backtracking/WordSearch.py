class Solution:

    marked = []

    def exist(self, board: List[List[str]], word: str) -> bool:
        letters = list(word);
        rowInd = 0;
        for row in board:
            ind = row.index(letters[0]);
            rowInd += 1;

    def find(self, board: List[List[str]], word: str, row: int, col: int) -> bool:
        