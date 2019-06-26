def removeDuplicates(nums):
    arr = {}
    for x in nums:
        arr[x] = 1
    return list(arr.keys())


print(removeDuplicates([1, 1, 2]))
