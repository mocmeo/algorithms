from collections import Counter


def relativeSortArray(arr1, arr2):
    numDict = Counter(arr1)
    result = []
    for num in arr2:
        if numDict[num] > 0:
            result.extend([num]*numDict[num])
            numDict[num] = 0

    for key in sorted(numDict.keys()):
        if numDict[key]:
            result.extend([key]*numDict[key])
    return result


print(relativeSortArray(
    [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))
