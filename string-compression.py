def updateResult(index, pos, chars):
    del chars[index:pos]
    length = pos - index + 1

    if length > 1:
        chars[index+1:index+1] = list(str(length))
        # chars.extend(index+1, list(str(length)))


def compress(chars):
    n = len(chars)
    if n <= 1:
        return n
    index = n-1
    pos = n-1
    while index > 0:
        if chars[index] != chars[index - 1]:
            updateResult(index, pos, chars)
            pos = index - 1
        index -= 1
        if index == 0:
            updateResult(index, pos, chars)
    return chars


print(compress(["a", "b", "b", "c", "c", "c", "d"]))
