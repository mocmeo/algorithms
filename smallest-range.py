import sys


def smallestRangeI(A, K):
    minNum, maxNum = min(A), max(A)

    result = 20000
    diff = maxNum - minNum
    for x in range(0, 2*K+1):
        result = min(result, abs(diff - x))

    return result


print(smallestRangeI([1], 0))
