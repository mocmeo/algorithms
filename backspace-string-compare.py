def process(myStr):
    i = 0
    result = []
    while i < len(myStr):
        if (myStr[i] == '#' and len(result) > 0):
            del result[-1]
        else:
            if (myStr[i] != '#'):
                result.append(myStr[i])
        i += 1
    return ''.join(result)


def backspaceCompare(S, T):
    S = process(S)
    T = process(T)
    print(S)
    print(T)
    return S == T


print(backspaceCompare("y#fo##f", "y#f#o##f"))
