def sortArrayByParity(A):
    oddArr = list(filter(lambda x: x % 2 != 0, A))
    evenArr = list(filter(lambda x: x % 2 == 0, A))
    return evenArr + oddArr


print(sortArrayByParity([3, 1, 2, 4]))
