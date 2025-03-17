import statistics
import sys

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Maybe the sum is at the max int value
        if sum(nums) < target:
            return 0;
        if sum(nums) == sys.max
        newTarget = sum(nums) - target;
        return self.traverse(newTarget, nums);

    def traverse(self, target: int, nums: List[int]) -> int:
        if (target == 0):
            return len(nums);
        if (target < 0):
            return len(nums) + 1;
        first = nums[0];
        last = nums[len(nums)-1];
        if first == last:
            return min(self.traverse(target-first, nums[1:]), self.traverse(target-last, nums[:len(nums)-1]));
        if first < last:
            return self.traverse(target-first, nums[1:]);
        return self.traverse(target-last, nums[:len(nums)-1]);
