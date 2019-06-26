def singleNumber(nums):
    numDict = {}
    for x in nums:
        if (numDict.get(x) is None):
            numDict[x] = 1
        else:
            numDict[x] += 1

    vals = list(numDict.values())
    for x in numDict.keys():
        if (vals.count(numDict[x]) == 1):
            return x


def singleNumber2(nums):
    result = nums[0]
    for x in range(1, len(nums)):
        result = result ^ nums[x]
    return result


print(singleNumber2([4, 1, 2, 1, 2]))
