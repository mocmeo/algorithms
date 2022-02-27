def chalkReplacer(chalk, k):
	modulo = k % sum(chalk)
	for i in range(len(chalk)):
		modulo -= chalk[i]
		if modulo < 0:
			return i

print(chalkReplacer([5,1,5], 22))
print(chalkReplacer([3,4,1,2], 25))