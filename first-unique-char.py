def firstUniqChar(s):
    strDict = {}
    for ch in s:
        if strDict.get(ch) is None:
            strDict[ch] = 1
        else:
            strDict[ch] += 1
    for i in range(len(s)):
        if strDict[s[i]] == 1:
            return i
    return -1


print(firstUniqChar("a"))
