def isIsomorphic(s, t):
    strDict = {}
    for i in range(0, len(s)):
        if (strDict.get(s[i]) is None):
            strDict[s[i]] = t[i]
        elif (strDict.get(s[i]) != t[i]):
            return False

    vals = list(strDict.values())
    for ch in strDict.values():
        if vals.count(ch) > 1:
            return False

    return True


print(isIsomorphic("aabb", "ccdd"))
