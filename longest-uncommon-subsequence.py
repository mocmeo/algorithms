
def findLUSlength(a, b):
    if a == b:
        return -1
    else:
        return max(len(a), len(b))


# print(findLUSlength("aefawfawfawfaw", "aefawfeawfwafwaef"))
print(findLUSlength("aaa", "aaa"))
print(findLUSlength("aba", "cdc"))
