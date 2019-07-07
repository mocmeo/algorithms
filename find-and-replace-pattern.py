def checkMatch(str1, pattern):
    strDict = {}
    for i in range(len(str1)):
        if strDict.get(str1[i]) is None:
            if pattern[i] in strDict.values():
                return False
            strDict[str1[i]] = pattern[i]
        else:
            if strDict[str1[i]] != pattern[i]:
                return False
    return True


def findAndReplacePattern(words, pattern):
    result = []
    for word in words:
        if checkMatch(word, pattern):
            result.append(word)

    return result


print(findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))
# print(findAndReplacePattern(["deq"], "abb"))
