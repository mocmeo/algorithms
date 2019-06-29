def isAnagram(s, t):
    if len(s) != len(t):
        return False
    sList = list(s)
    sList.sort()
    tList = list(t)
    tList.sort()

    for i in range(0, len(sList)):
        if (sList[i] != tList[i]):
            return False
    return True


print(isAnagram("rat", "car"))
