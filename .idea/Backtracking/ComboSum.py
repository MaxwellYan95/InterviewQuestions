class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = [];
        if (target < min(candidates)):
            return [[]];
        for num in candidates:
            if target == num:
                return [[num]];
            lst = self.combinationSum(candidates, target-num)
            for innerLst in lst:
                innerLstCopy = innerLst.copy();
                innerLstCopy.append(num);
                result.append(innerLstCopy);
        return result;

sol = Solution();
lst = sol.combinationSum([2,3,6,7], 7);
print(lst);