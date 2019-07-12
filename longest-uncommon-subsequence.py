from collections import Counter


def findLUSlength(a, b):
    strDict = Counter(b)
    result = ""
    for ch in a:
        if strDict[ch] == 0:
            result += ch

    if not result:
        return -1
    else:
        return result


print(findLUSlength("aefawfawfawfaw", "aefawfeawfwafwaef"))
