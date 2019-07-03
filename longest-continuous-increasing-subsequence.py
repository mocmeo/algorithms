def findLengthOfLCIS(nums):
    if not nums:
        return 0

    resultMax = 1
    curLength = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            curLength += 1
            resultMax = max(resultMax, curLength)
        else:
            curLength = 1
    return resultMax


print(findLengthOfLCIS([2, 2, 2, 2, 2]))
