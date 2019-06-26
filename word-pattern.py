def wordPattern(pattern, str):
    strs = str.split(' ')
    if (len(pattern) != len(strs)):
        return False

    strDict = {}

    for i in range(0, len(pattern)):
        if (strDict.get(pattern[i]) is None):
            strDict[pattern[i]] = strs[i]
        elif strDict.get(pattern[i]) != strs[i]:
            return False

    vals = list(strDict.values())
    for word in strDict.values():
        if vals.count(word) > 1:
            return False
    return True


print(wordPattern("abba", "dog dog dog dog"))
