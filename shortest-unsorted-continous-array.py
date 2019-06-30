def findUnsortedSubarray(nums):
    sortedArr = nums[:]
    sortedArr.sort()

    left = 0
    right = len(nums) - 1

    while (left < right):
        isContinue = False
        if sortedArr[left] == nums[left]:
            left += 1
            isContinue = True
        if sortedArr[right] == nums[right]:
            right -= 1
            isContinue = True

        if (not isContinue):
            break

    if left == right:
        return 0
    return right - left + 1


print(findUnsortedSubarray([1]))
