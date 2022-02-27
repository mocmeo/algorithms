def numRescueBoats(people, limit):
	people = sorted(people)
	l = 0
	r = len(people)-1
	res = 0
	while l <= r:
		if people[r] + people[l] > limit:
			r -= 1
		else:
			r -= 1
			l += 1
		res += 1
	return res

print(numRescueBoats([1, 2], 3))
print(numRescueBoats([3,2,2,1], 3))
print(numRescueBoats([3,2,2,1], 3))
print(numRescueBoats([3,5,3,4], 5))
		

