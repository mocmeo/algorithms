from collections import Counter


def findPairs(nums, k):
    if len(nums) <= 1 or k < 0:
        return 0
    nums.sort()
    n = len(nums)

    x, y = 0, 1
    result = set([])
    while x < n and y < n:
        while y < n and nums[y] < nums[x] + k or y <= x:
            y += 1
        if y < n and nums[y] == nums[x] + k:
            if x < y:
                result.add((nums[x], nums[y]))

        oldX = nums[x]
        while x < n and nums[x] == oldX:
            x += 1
    return result


def findPairs2(nums, k):
    if k < 0:
        return 0

    count = Counter(nums)
    pairs = set([])
    for num in count.keys():
        if k == 0:
            if count[num] > 1:
                pairs.add((num, num))
        else:
            otherNum = num + k
            if count[otherNum] > 0:
                pairs.add((num, otherNum) if num <
                          otherNum else (otherNum, num))
    return len(pairs)


print(findPairs2([1, 1, 1, 2, 2], 0))
print(findPairs2([3, 1, 4, 1, 5], 2))
print(findPairs2([1, 2, 3, 4, 5], 1))
print(findPairs2([1, 3, 1, 5, 4], 0))
