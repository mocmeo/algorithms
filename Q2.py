def sumOfThree(num):
	if (num - 3) % 3 != 0:
		return []

	x = (num - 3) / 3
	return [x, x+1,x+2]

print(sumOfThree(33))
print(sumOfThree(0))