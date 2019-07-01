def thirdMax(nums):
    nums = list(set(nums))
    if len(nums) < 3:
        return max(nums)

    first = nums.remove(max(nums))
    second = nums.remove(max(nums))
    return max(nums)


print(thirdMax([2, 2, 3]))
