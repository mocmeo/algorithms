def containsNearbyDuplicate(nums, k):
    # numDict: (key, value) => (number, index)
    numDict = {}

    for x in range(0, len(nums)):
        currentNumber = nums[x]
        if (numDict.get(currentNumber) is not None):
            if (abs(x - numDict[currentNumber] <= k)):
                return True
        numDict[currentNumber] = x
    return False


print(containsNearbyDuplicate([1, 2, 3, 1], 3))
