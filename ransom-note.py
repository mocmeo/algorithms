def canConstruct(ransomNote, magazine):
    magazineDict = {}
    for ch in magazine:
        if magazineDict.get(ch) is None:
            magazineDict[ch] = 1
        else:
            magazineDict[ch] += 1

    for ch in ransomNote:
        if magazineDict.get(ch) is None or magazineDict[ch] == 0:
            return False
        else:
            magazineDict[ch] -= 1
    return True


print(canConstruct("aa", ""))
