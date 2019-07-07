def groupAnagrams(strs):
    strDict = {}
    for val in strs:
        sVal = "".join(sorted(val))
        if strDict.get(sVal) is None:
            strDict[sVal] = [val]
        else:
            strDict[sVal].append(val)

    result = []
    for key in strDict.keys():
        anagrams = strDict[key]
        result.append(anagrams)
    return result


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
