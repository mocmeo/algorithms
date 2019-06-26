import sys


def removeElement(nums, val):
    for x in range(0, len(nums)):
        if (nums[x] == val):
            nums[x] = sys.maxsize

    nums.sort()
    if (sys.maxsize in nums):
        pos = nums.index(sys.maxsize)
        nums = nums[0:pos]
        return len(nums)
    else:
        return len(nums)
