def checkValidPrefix(strs, length):
    firstStr = strs[0]
    prefix = firstStr[0:int(length) + 1]

    for indexStr in strs:
        if (not indexStr.startswith(prefix)):
            return False
    return True


def binarySearch(strs):
    left = 0
    right = len(strs[0]) - 1
    result = -1

    while left <= right:
        mid = int((left + right) / 2)

        if (checkValidPrefix(strs, mid)):
            result = max(result, mid)
            left = mid + 1
        else:
            right = mid - 1

    return result


def longestCommonPrefix(strs):
    if (len(strs) == 0):
        return ""

    length = binarySearch(strs)
    return strs[0][0:int(length) + 1]


print(longestCommonPrefix(['a']))
