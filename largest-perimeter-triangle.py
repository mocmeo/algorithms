def largestPerimeter(A):
    A.sort()
    if len(A) < 3:
        return 0

    while len(A) >= 3:
        x, y, z = A[-1], A[-2], A[-3]
        if (x + y > z and y + z > x and x + z > y):
            return x+y+z
        A.pop()
    return 0


print(largestPerimeter([3, 6, 2, 3]))
