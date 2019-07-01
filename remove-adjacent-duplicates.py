def removeDuplicates(S):
    if len(S) == 0:
        return ""
    S = S + " "
    stack = []
    stack.append(S[0])

    count = 1
    for i in range(1, len(S)):
        if S[i] != S[i-1]:
            while len(stack) >= 2 and stack[-2:].count(S[i-1]) >= 2:
                stack.pop()
                stack.pop()
        stack.append(S[i])
    return "".join(stack).strip()


def removeDuplicates2(S):
    if not S:
        return ""

    stack = []
    for x in S:
        if stack:
            if stack[-1] == x:
                stack.pop()
            else:
                stack.append(x)
        else:
            stack.append(x)
    return "".join(stack)


print(removeDuplicates2("aaaaaaaaa"))
print(removeDuplicates2("aaaaaaaa"))
