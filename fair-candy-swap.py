from collections import Counter


def fairCandySwap(A, B):
    countA, countB = Counter(A), Counter(B)
    sumA, sumB = sum(A), sum(B)
    diff = int(abs(sumA - sumB)/2)
    if sumA < sumB:
        for num in countA.keys():
            if countB[num + diff] > 0:
                return [num, num + diff]
    else:
        for num in countB.keys():
            if countA[num + diff] > 0:
                return [num + diff, num]


print(fairCandySwap([1, 2, 5], [2, 4]))
