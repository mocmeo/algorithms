import string


def reverseOnlyLetters(S):
    strS = ""
    result = ""
    for x in S:
        if x in string.ascii_letters:
            strS += x

    count = 0
    strS = strS[::-1]
    for x in S:
        if x not in string.ascii_letters:
            result += x
        else:
            result += strS[count]
            count += 1
    return result


print(reverseOnlyLetters("a-bC-dEf-ghIj"))
