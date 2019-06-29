import sys


def removeDuplicates(nums):
    for i in range(1, len(nums)):
        if (nums[i] == nums[i-1]):
            nums[i-1] = sys.maxsize

    nums.sort()
    if (sys.maxsize in nums):
        pos = nums.index(sys.maxsize)
        nums = nums[0:pos]
    return len(nums)


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
