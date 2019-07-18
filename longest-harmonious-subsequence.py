from collections import Counter


def findLHS(nums):
    numDict = Counter()
    for num in nums:
        if not numDict[num]:
            numDict[num] = [[num], [num]]
        else:
            numDict[num][0].append(num)
            numDict[num][1].append(num)

        if numDict[num-1]:
            numDict[num-1][1].append(num)
        if numDict[num+1]:
            numDict[num+1][0].append(num)

    result = 0
    for key in numDict.keys():
        min1 = min(numDict[key][0])
        max1 = max(numDict[key][0])
        max2 = max(numDict[key][1])
        min2 = min(numDict[key][1])

        if max1 - min1 == 1:
            result = max(result, len(numDict[key][0]))
        if max2 - min2 == 1:
            result = max(result, len(numDict[key][1]))
    return result


def findLHS2(nums):
    numDict = Counter(nums)
    result = 0

    for key in numDict.keys():
        if numDict[key+1]:
            result = max(result, numDict[key] + numDict[key+1])
        if numDict[key-1]:
            result = max(result, numDict[key] + numDict[key-1])
    return result


print(findLHS2([1, 2, 1, 3, 0, 0, 2, 2, 1, 3, 3]))
print(findLHS2([1, 3, 2, 2, 5, 2, 3, 7]))
print(findLHS2([1, 1, 1, 1]))
