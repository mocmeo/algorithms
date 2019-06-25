def containDuplicate(nums):
    if (len(nums) <= 1):
        return False

    nums.sort()
    for x in range(0, len(nums) - 1):
        if (nums[x] == nums[x+1]):
            return True
    return False


print(containDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
