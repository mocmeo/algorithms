def minAddToMakeValid(S):
    stack = []
    for ch in S:
        if ch == '(':
            stack.append(ch)
        else:
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(ch)
    return len(stack)


print(minAddToMakeValid(""))
