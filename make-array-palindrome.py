def solution(arr, n):
    result = 0
    x, y = 0, n-1

    while x < y:
        if arr[x] == arr[y]:
            x += 1
            y -= 1
        elif arr[x] < arr[y]:
            arr[x+1] = arr[x] + arr[x+1]
            result += 1
            x += 1
        elif arr[y] < arr[x]:
            arr[y-1] = arr[y] + arr[y-1]
            result += 1
            y -= 1
    return result


print(solution([2, 2, 3], 1))
