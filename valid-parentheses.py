def getOpeningBracket(ch):
    if ch == ')':
        return '('
    if ch == '}':
        return '{'
    if ch == ']':
        return '['


def isValid(s):
    stack = []
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if len(stack) == 0:
                return False
            if stack[-1] != getOpeningBracket(ch):
                return False
            else:
                stack.pop()
    if len(stack) > 0:
        return False
    return True


print(isValid("{[]}"))
