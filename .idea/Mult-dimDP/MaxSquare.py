class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        maximum = 0;
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == '1':
                    side = self.traverse(matrix, row, col);
                    maximum = max(maximum, side*side);
        return maximum;

    def traverse(self, matrix: list[list[str]], row: int, col: int):
        if not(0<=row<len(matrix)) or not(0<=col<len(matrix[0])):
            return 0;
        if matrix[row][col] == '0':
            return 0;
        right = self.traverse(matrix, row, col+1);
        down = self.traverse(matrix, row+1, col);
        diagonal = self.traverse(matrix, row+1, col+1);
        return 1 + min(right, down, diagonal);