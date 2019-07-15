def findMaxLength(nums):
    numDict = {}
    numDict[0] = -1
    count = 0
    maxLen = 0

    for i, num in enumerate(nums):
        count += 1 if num == 1 else -1
        if numDict.get(count) is None:
            numDict[count] = i
        else:
            maxLen = max(maxLen, i - numDict[count])
    return maxLen


print(findMaxLength([1, 0]))
