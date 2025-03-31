class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        height = len(matrix);
        width = len(matrix[0]);
        dp = [[0 for j in range(width)] for i in range(height)];
        maxSide = 0;
        for y in range(height):
            for x in range(width):
                if matrix[y][x] == '1':
                    if x==0 or y==0:
                        dp[y][x] = 1;
                    else:
                        dp[y][x] = min(dp[y-1][x], dp[y][x-1], dp[y-1][x-1]) + 1;
                    maxSide = max(maxSide, dp[y][x]);
        return maxSide*maxSide;

