def majorityElement(nums):
    if (len(nums) == 1):
        return nums[0]

    numDict = {}
    for x in nums:
        if (numDict.get(x) is None):
            numDict[x] = 1
        else:
            numDict[x] += 1
            if (numDict[x] > int(len(nums) / 2)):
                return x


def majorityElement2(nums):
    for num in set(nums):
        if nums.count(num) > int(len(nums) / 2):
            return num


print(majorityElement2([2, 2, 1, 1, 1, 2, 2]))
