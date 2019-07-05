from collections import Counter


def threeSum(nums):
    if len(nums) < 3:
        return []
    numDict = Counter(nums)
    triplets = set([])
    if numDict[0] >= 3:
        triplets.add((0, 0, 0))
    if numDict[0] > 0:
        for num in numDict.keys():
            if num > 0:
                otherNum = -num
                if numDict[otherNum]:
                    triplets.add((0, otherNum, num))

    # 1 negative, 2 positive
    for num in numDict.keys():
        reversedNum = -num
        sign = 1 if num > 0 else -1

        for x in numDict.keys():
            y = reversedNum - x
            if x == y and x != 0 and numDict[x] >= 2:
                triplets.add((num, x, y))
            if sign == -1 and x > 0 and y > x and numDict[y] > 0:
                triplets.add((num, x, y))
            if sign == 1 and x < 0 and y < x and numDict[y] > 0:
                triplets.add((num, x, y))
    return list(triplets)


print(threeSum([-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]))
