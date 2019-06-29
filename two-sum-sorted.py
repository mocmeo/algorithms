def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1
    result = -1
    while (left <= right):
        mid = int((left + right) / 2)
        if nums[mid] <= target:
            left = mid + 1
            if (nums[mid] == target):
                result = max(result, mid)
        elif nums[mid] > target:
            right = mid - 1
    return result


def twoSum(numbers, target):
    for i in range(0, len(numbers)):
        j = binarySearch(numbers, target - numbers[i])
        if (j != -1):
            return [i+1, j+1]


print(twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8))
