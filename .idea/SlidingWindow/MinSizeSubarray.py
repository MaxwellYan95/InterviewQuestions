import statistics

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        avg = statistics.mean(nums);
        approxSize = int(target/avg) + 1;
        if sum(nums) < target:
            return 0;
        if sum(nums) == target:
            return len(nums);

        return self.traverse(newTarget, nums, approxSize);

    def traverse(self, nums: list[int], begInd: int, endInd: int, approxSize: int, target: int) -> int:
        if (approxSize == len(nums)):

        else:
            first = nums[begInd];
            last = nums[endInd];
            if first == last:
                return min(self.traverse(nums, begInd+1, endInd, approxSize, target), self.traverse(nums, begInd, endInd-1, approxSize, target));
            if first < last:
                return self.traverse(nums, begInd+1, endInd, approxSize, target);
            return self.traverse(nums, begInd, endInd-1, approxSize, target);

    def fineTuning(self, nums: list[int], begInd: int, endInd: int, approxSize: int, target: int) -> int:
        curSum = sum(nums);
        curSize = len(nums);
        while True:
            if curSum >= target:
                break;
            if begInd == -1:
                curSum = curSum + last;
                curSize = curSize + 1;
                endInd = endInd + 1;
                continue;
            if endInd == len(nums):
                curSum = curSum + first;
                curSize = curSize + 1;
                begInd = begInd - 1;
                continue;
            first = nums[begInd];
            last = nums[endInd];
            if first == last:
                if curSum + first + last <= target:
                    curSum = curSum + first + last;
                    curSize = curSize + 2;
                    begInd = begInd - 1;
                    endInd = endInd + 1;
                else:
                    return curSize + 1;
            elif first > last:
                curSum = curSum + first;
                curSize = curSize + 1;
                begInd = begInd - 1;
            else:
                curSum = curSum + last;
                curSize = curSize + 1;
                endInd = endInd + 1;
        return curSize;
