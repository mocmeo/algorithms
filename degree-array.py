def findShortestSubArray(nums):
    numDict = {}
    degree = 0
    for i in range(len(nums)):
        x = nums[i]
        if numDict.get(x) is None:
            numDict[x] = [1, i, i]
        else:
            numDict[x][0] += 1
            numDict[x][1] = min(numDict[x][1], i)
            numDict[x][2] = max(numDict[x][2], i)
        degree = max(degree, numDict[x][0])

    result = len(nums)
    for key in numDict.keys():
        val = numDict[key]
        if val[0] == degree:
            result = min(result, val[2] - val[1] + 1)
    return result


print(findShortestSubArray([2, 1]))
