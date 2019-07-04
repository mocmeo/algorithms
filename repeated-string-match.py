def repeatedStringMatch(A, B):
    myStr = ""
    while len(myStr) < len(B):
        myStr += A
        if B in myStr:
            return int(len(myStr) / len(A))

    myStr += A
    if B in myStr:
        return int(len(myStr) / len(A))
    return -1


print(repeatedStringMatch("abc", "cabcabca"))
