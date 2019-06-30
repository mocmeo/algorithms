import string


def commonChars(A):
    result = ""
    for ch in string.ascii_lowercase:
        minOccur = 100
        for item in A:
            minOccur = min(minOccur, item.count(ch))
        result += ch * minOccur
    return list(result)


print(commonChars(["cool", "lock", "cook"]))
