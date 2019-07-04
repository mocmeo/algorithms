def sortArrayByParityII(A):
    oddArr = list(filter(lambda x: x % 2 != 0, A))
    evenArr = list(filter(lambda x: x % 2 == 0, A))
    result = []
    for i in range(len(oddArr)):
        result.append(evenArr[i])
        result.append(oddArr[i])
    return result


print(sortArrayByParityII([4, 2, 5, 7]))
