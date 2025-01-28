def reverseBits(n: int) -> int:
    bitList = list(str(n))
    bitListReverse = reversed(bitList)
    bitString = "".join(bitListReverse)
    return int(bitString)

print(reverseBits(10100101000001111010011100))
