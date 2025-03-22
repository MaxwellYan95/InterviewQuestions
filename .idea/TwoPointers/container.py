def maxArea(height: list[int]) -> int:
    n = len(height);
    maximum = 0;
    maxLeft = height[0];
    maxLeftIndex = 0;
    for i in range(1, n):
        if maxLeft < height[i]:
            maxLeft = height[i];
            maxLeftIndex = i;
        else:
            break

    for i in range(maxLeftIndex+1, n):
        area = (min(maxLeft, height[i])) * abs(maxLeftIndex - i);
        maximum = max(maximum, area);

    maxRight = height[0];
    maxRightIndex = 0;
    for i in range(n-2, -1, -1):
        if maxRight < height[i]:
            maxRight = height[i];
            maxRightIndex = i;
        else:
            break

    for i in range(maxRightIndex-1, -1, 0):
        area = (min(maxRight, height[i])) * abs(maxRightIndex - i);
        maximum = max(maximum, area);


h = [1,8,6,2,5,4,8,3,7]
maxArea(h)


