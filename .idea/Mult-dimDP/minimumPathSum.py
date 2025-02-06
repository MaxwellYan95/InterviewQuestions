class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return grid[0][0];
        if len(grid) == 1:
            recur = minPathSum(grid[0][:len(grid[0])-1]);
        if len(grid[0]) == 1:
            recur = minPathSum(grid[:len(grid)-1]);


sol = Solution();
print(sol.minPathSum([[1,2,3],[4,5,6]]))