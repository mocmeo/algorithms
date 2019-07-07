def nextGreaterElement(nums1, nums2):
    result = []
    for num in nums1:
        pos = nums2.index(num)
        if pos == len(nums2) - 1:
            result.append(-1)
        else:
            found = False
            for i in range(pos+1, len(nums2)):
                if nums2[i] > num:
                    result.append(nums2[i])
                    found = True
                    break
            if not found:
                result.append(-1)
    return result


print(nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
print(nextGreaterElement([2, 4], [1, 2, 3, 4]))
