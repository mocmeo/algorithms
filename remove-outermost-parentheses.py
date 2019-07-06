def removeOuterParentheses(S):
    count = 0
    result = ""
    prev = 0
    for i in range(len(S)):
        if S[i] == '(':
            count += 1
        else:
            count -= 1
            if count == 0:
                primitive = S[prev:i+1]
                if len(primitive) > 2:
                    result += primitive[1:-1]
                prev = i+1
    return result


print(removeOuterParentheses("(())"))
