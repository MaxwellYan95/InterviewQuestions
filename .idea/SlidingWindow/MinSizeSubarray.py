import statistics
import sys

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        total = sum(nums);
        return self.traverse(target, nums, total);

    def traverse(self, target: int, nums: list[int], total: int) -> int:
        left = 0;
        right = len(nums)-1;
        while left < right:
            if nums[left] < nums[right]:
                left = left + 1;
                total = total - nums[left];
            elif nums[left] > nums[right]:
                right = right - right;
                total = total - nums[right];
            else:
                leftCall = self.traverse(target, nums[left+1: right], total)
                if leftCall != 0:
                    return leftCall;
                else:
                    rightCall = self.traverse(target, nums[left: right-1], total)
                    if rightCall != 0:
                        return rightCall;
                    else:
                        break;
            if total < target:
                return right - left + 1;
        return 0;