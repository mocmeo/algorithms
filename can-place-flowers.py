def canPlaceFlowers(flowerbed, n):
    if not flowerbed:
        return False
    prev = float('-inf')
    arr = []
    result = 0
    for i, val in enumerate(flowerbed):
        if val == 1:
            prev = i
        arr.append(i - prev)

    prev = float('inf')
    for i in range(len(flowerbed)-1, -1, -1):
        if flowerbed[i] == 1:
            prev = i
        arr[i] = min(arr[i], prev - i)
        if arr[i] > 0 and arr[i] % 2 == 0:
            if i == 0 or (i > 0 and arr[i-1] % 2 != 0):
                result += 1

    if prev == float('inf'):
        result = int(len(flowerbed)/2 +
                     1) if len(flowerbed) % 2 != 0 else int(len(flowerbed)/2)
    return result >= n


print(canPlaceFlowers([1, 0, 0, 0, 0, 1], 1))
