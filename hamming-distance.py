def hammingDistance(x, y):
    bit_x = getBits(x)
    bit_y = getBits(y)
    while len(bit_x) < len(bit_y):
        bit_x.insert(0, 0)
    while len(bit_y) < len(bit_x):
        bit_y.insert(0, 0)

    answer = 0
    for i in range(len(bit_x)):
        answer += abs(bit_x[i] - bit_y[i])
    return answer


def getBits(num):
    bit = 1
    result = []
    while num >= bit:
        if num & bit:
            result.insert(0, 1)
        else:
            result.insert(0, 0)
        bit <<= 1
    return result


print(hammingDistance(1, 0))
