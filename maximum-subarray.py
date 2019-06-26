import sys


def maxSubArray(nums):
    result = nums[0]
    sumArr = nums[0]
    j = 0
    for i in range(1, len(nums)):
        sumArr += nums[i]
        while (j < i and (sumArr < 0 or nums[j] < 0)):
            sumArr -= nums[j]
            j += 1
        result = max(result, sumArr)
    return result


def maxSubArray2(nums):
    sumArr = maxSum = nums[0]
    for i in range(1, len(nums)):
        sumArr = max(nums[i], sumArr + nums[i])
        maxSum = max(maxSum, sumArr)
    return maxSum
