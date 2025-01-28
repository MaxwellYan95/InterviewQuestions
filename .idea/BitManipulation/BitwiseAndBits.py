def rangeBitwiseAnd(left: int, right: int) -> int:
    leftCopy = left
    leftBits = []
    rightCopy = right
    rightBits = []
    andBits = []
    for pow in range(30, -1, -1):
        if 2**pow <= leftCopy:
            leftBits.append(1)
            leftCopy = leftCopy - 2**pow
        else:
            leftBits.append(0)
        if 2**pow <= rightCopy:
            rightBits.append(1)
            rightCopy = rightCopy - 2**pow
        else:
            rightBits.append(0)

    max = 30
    result = 0
    for index in range(len(leftBits)):
        if leftBits[index] == 1 and rightBits[index] == 1:
            result = result + 2**max
        max = max - 1
    return result

print(rangeBitwiseAnd(5, 7))