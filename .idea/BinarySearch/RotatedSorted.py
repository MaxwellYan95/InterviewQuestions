class Solution:
    def search(self, nums: list[int], target: int) -> int:

        return self.traverse(nums, target);

    def findIndex(self, nums: list[int]):
        if len(nums) == 1:
            return 0;
        elif len(nums) == 2:
            if nums[0] < nums[1]:
                return 1;
        if nums[0] < nums[len(nums)-1]:
            return len(nums)-1;
        middleIndex = int(len(nums)/2);
        if (nums[middleIndex-1] < nums[middleIndex] and nums[middleIndex] > nums[middleIndex+1]):
            return middleIndex;
        elif (nums[middleIndex-1] > nums[middleIndex] and nums[middleIndex] < nums[middleIndex+1]):
            return middleIndex-1;
        if (nums[middleIndex] > nums[len(nums)-1]):
            return self.findIndex(nums[middleIndex:]) + middleIndex;
        return self.findIndex(nums[:middleIndex+1]);

def traverse(self, nums: list[int], target: int) -> int:
        if len(nums) == 0:
            return -1;
        elif len(nums) == 1:
            if nums[0] == target:
                return 0;
            return -1;
        elif len(nums) == 2:
            if nums[0] == target:
                return 0;
            elif nums[1] == target:
                return 1;
            return -1;
        middleIndex = int(len(nums)/2);
        if (nums[middleIndex-1] < nums[middleIndex] and nums[middleIndex] > nums[middleIndex+1]):
            left = self.traverse(nums[:middleIndex+1], target);
            if left == -1:
                right = self.traverse(nums[middleIndex:], target);
                if right == -1:
                    return -1;
                return middleIndex + right;
            else:
                return left;
        else:
            leftDiff = abs(nums[middleIndex-1] - target);
            rightDiff = abs(nums[middleIndex+1] - target);
            if leftDiff < rightDiff:
                return self.traverse(nums[:middleIndex+1], target);
            else:
                right = self.traverse(nums[middleIndex:], target);
                if right == -1:
                    return -1;
                return middleIndex + right;

sol = Solution();
print(sol.search([4,5,6,7,0,1,2], 3));
print(sol.search([6,7,1,2,3,4,5], 6));
print();