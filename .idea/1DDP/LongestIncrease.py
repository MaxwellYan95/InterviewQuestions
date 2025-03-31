class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return len(nums);
        lst = [nums[len(nums)-1]];
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < lst[len(lst)-1]:
                lst.append(nums[i]);
        return len(lst);

sol = Solution();
print(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]));