class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sortPoints = sorted(points, key=lambda p: p[0]);
        end = sortPoints[0][1];
        balloons = 1;
        for p in sortPoints:
            if (p[0] > end):
                balloons += 1;
                end = p[1];
            else:
                end = min(end, p[1]);
        return balloons;