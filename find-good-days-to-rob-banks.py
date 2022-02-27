from tkinter import N


def goodDaysToRobBank(security, time):
	n = len(security)
	left = [0]*n
	right = [0]*n
	res = []
	for i in range(1, n):
		if security[i-1] >= security[i]:
			left[i] = left[i-1] + 1
		else:
			left[i] = 0
		
	for i in range(n-2,-1,-1):
		if security[i+1] >= security[i]:
			right[i] = right[i+1] + 1
		else:
			right[i] = 0

	for i in range(n):
		if min(left[i], right[i]) >= time:
			res.append(i)

	return res

print(goodDaysToRobBank([5,3,3,3,5,6,2], 2))
print(goodDaysToRobBank([1,1,1,1,1], 0))
print(goodDaysToRobBank([1,2,3,4,5,6], 2))
