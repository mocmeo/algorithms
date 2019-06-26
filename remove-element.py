import sys


def removeElement(nums, val):
    for x in range(0, len(nums)):
        if (nums[x] == val):
            nums[x] = sys.maxsize

    nums.sort()
    if (sys.maxsize in nums):
        pos = nums.index(sys.maxsize)
        num = nums[0:pos]
        return len(num)
    else:
        return 0


print(removeElement([2], 3))
