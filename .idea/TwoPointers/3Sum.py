#def threeSum(self, nums: List[int]) -> List[List[int]]:
#    results = []
#    for first in range(0, len(nums)-2):
#        for second in range(first+1, len(nums)-1):
#            for third in range(second+1, len(nums)):
#                if (nums[first]+nums[second]+nums[third]) == 0:
#                    list = sorted([nums[first], nums[second], nums[third]])
#                    if list not in results:
#                        results.append(list)
#    return results

def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort();
    lst = [];
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j = i+1;
        k = len(nums)-1;
        while j < k:
            curSum = nums[i] + nums[j] + nums[k];
            combo = [nums[i], nums[j], nums[k]];
            if curSum > 0:
                k -= 1;
            elif curSum < 0:
                j += 1;
            else:
                lst.append(combo);
                j += 1;
                while nums[j] == nums[j-1] and j < k:
                    j += 1;
    return lst;

print(threeSum([-1,0,1,2,-1,-4]));


