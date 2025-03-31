from collections import defaultdict
from email.policy import default


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        if len(points) <= 2:
            return len(points);
        ans = 1;
        for index in range(len(points)-1):
            one = points[index];
            hash = defaultdict(int);
            for inner in range(index+1, len(points)):
                two = points[inner];
                s = self.slope(one, two);
                b = self.startingPoint(one, two);
                hash[(s, b)] += 1;
                ans = max(hash[(s, b)], ans);
        return ans+1;

    def slope(self, onePoint: list[int], twoPoint: list[int]):
        if (onePoint[0]-twoPoint[0]) == 0:
            return None;
        return (onePoint[1]-twoPoint[1]) / (onePoint[0]-twoPoint[0]);

    def startingPoint(self, onePoint: list[int], twoPoint: list[int]):
        s = self.slope(onePoint, twoPoint);
        if (s == None):
            return None;
        b = onePoint[1] - s*onePoint[0];
        return b;

sol = Solution();
print(sol.maxPoints([[1,1],[2,2],[3,3]]));
print(sol.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]));
