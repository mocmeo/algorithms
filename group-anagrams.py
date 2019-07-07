def groupAnagrams(strs):
    strDict = {}
    for i, val in enumerate(strs):
        sVal = "".join(sorted(val))
        if strDict.get(sVal) is None:
            strDict[sVal] = [i]
        else:
            strDict[sVal].append(i)

    result = []
    for key in strDict.keys():
        anagrams = []
        for index in strDict[key]:
            anagrams.append(strs[index])
        result.append(anagrams)
    return result


print(groupAnagrams(["eat"]))
