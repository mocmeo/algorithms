from collections import Counter

def asteroidsDestroyed(mass, asteroids):
	count = Counter(asteroids)
	max_asteroid = max(asteroids)

	for i in range(1, max_asteroid+1):
		if count[i]:
			if mass < i:
				return False
			else:
				mass += i*count[i]
	return True

print(asteroidsDestroyed(10, [3,9,19,5,21]))
print(asteroidsDestroyed(5, [4,9,23,4]))
  