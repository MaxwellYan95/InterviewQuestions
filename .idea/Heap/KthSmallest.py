class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if len(nums1) == 1 and len(nums2) == 1:
            return [[nums1[0], nums2[0]]];
        results = [];
        if (nums1[len(nums1)-1] < nums2[len(nums2)-1]):
            results = self.kSmallestPairs(nums1, nums2[:len(nums2)-1]);
        else:
            results = self.kSmallestPairs(nums1[:len(nums1)-1], nums2);
