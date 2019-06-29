def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    result = 0
    while (left <= right):
        mid = int((left + right)/2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            result = max(result, mid+1)
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return result


print(searchInsert([1, 3, 5, 6], 0))
