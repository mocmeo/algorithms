def reverseString(s):
    for i in range(0, int(len(s) / 2)):
        j = len(s)-i-1
        s[i], s[j] = s[j], s[i]
    return s


print(reverseString(["h", "e", "l", "l", "o"]))
