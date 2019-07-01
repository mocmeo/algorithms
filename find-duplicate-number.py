def findDuplicate(nums):
    for x in set(nums):
        if (nums.count(x) > 1):
            return x


print(findDuplicate([3, 1, 3, 4, 2]))
