class Solution:
    def rob(self, nums: list[int]) -> int:
        return self.reverseRob(reversed(nums));

    def reverseRob(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0;
        elif len(nums) == 1:
            return nums[0];
        elif len(nums) == 2:
            return max(nums[0], nums[1]);
        elif nums[0]+nums[2] > nums[1]:
            return nums[0] + self.rob(nums[2:])
        return self.rob(nums[1:]);

sol = Solution();
sol.rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]);