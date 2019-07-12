def maxDepthAfterSplit(seq):
    countSeq = []
    result = [0]*len(seq)
    count = 0
    maxDepth = 0
    for ch in seq:
        if ch == '(':
            count += 1
        else:
            count -= 1
        countSeq.append(count)
        maxDepth = max(maxDepth, count)

    avgDept = int(maxDepth/2) + 1
    x = 0
    y = 0
    yy = 0
    while x < len(seq) and countSeq[x] < avgDept:
        x += 1

    y = x
    while y < len(seq) and countSeq[y] != 0:
        y += 1
        if countSeq[y] == avgDept-1:
            yy = max(yy, y)
    for i in range(x, yy+1):
        result[i] = 1
    return result


print(maxDepthAfterSplit("(((()))((())))"))
