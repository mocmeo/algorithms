def coinChange(coins, amount):
	coins = sorted(coins)
	F = [100000]*(amount + 1)
	F[0] = 0
	for coin in coins:
		if amount >= coin:
			F[coin] = 1

	for i in range(amount+1):
		for coin in coins:
			if i - coin > 0:
				F[i] = min(F[i], 1 + F[i-coin])

	if F[-1] == 100000:
		return -1
	return F[-1]

print(coinChange([1,2,5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))
print(coinChange([2], 1))