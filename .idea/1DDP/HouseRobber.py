class Solution:
    def rob(self, nums: list[int]) -> int:
        nums.reverse();
        reverseAns = self.reverseRob(nums);
        nums.reverse();
        ans = self.reverseRob(nums);
        return max(reverseAns, ans);

    def reverseRob(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0;
        elif len(nums) == 1:
            return nums[0];
        elif len(nums) == 2:
            return max(nums[0], nums[1]);
        elif len(nums) == 3:
            return max(nums[0]+nums[2], nums[1]);
        elif (nums[0]+nums[3] >= nums[1]+nums[3]) and (nums[0]+nums[3] >= nums[0]+nums[2]):
            oneWay = nums[0] + nums[3] + self.reverseRob(nums[5:]);
            twoWay = nums[0] + nums[2] + self.reverseRob(nums[4:]);
            return max(oneWay, twoWay);
        elif nums[0]+nums[2] == nums[1]+nums[3]:
            oneWay = nums[0] + nums[2] + self.reverseRob(nums[4:]);
            twoWay = nums[1] + nums[3] + self.reverseRob(nums[5:]);
            return max(oneWay, twoWay);
        elif nums[0]+nums[2] > nums[1]+nums[3]:
            return nums[0] + nums[2] + self.reverseRob(nums[4:]);
        return nums[1] + nums[3] + self.reverseRob(nums[5:]);

sol = Solution();
sol.rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]);