def maxArea(height: list[int]) -> int:
    area = 0;
    sortedLst = sorted(height, reverse=True)
    lst = height
    while len(lst) >= 2:
        firstValue = lst[0]
        lastValue = lst[len(lst)-1]
        newArea = 0;
        if firstValue < lastValue:
            newArea = firstValue*len(lst)
            lst = lst[1:len(lst)]
        else:
            newArea = lastValue*len(lst)
            lst = lst[0:len(lst)-1]
        if area < newArea:
            area = newArea
    return area

h = [1,8,6,2,5,4,8,3,7]
maxArea(h)


