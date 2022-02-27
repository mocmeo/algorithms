from operator import itemgetter


def carPooling(trips, capacity):
	map_pick = {}
	map_drop = {}
	max_dest = 0

	for t in trips:
		k, x, y = t[0], t[1], t[2]
		map_pick[x] = map_pick.get(x, 0) + k
		map_drop[y] = map_drop.get(y, 0) + k
		max_dest = max(max_dest, y)

	acc = 0
	for i in range(max_dest+1):
		acc = acc + map_pick.get(i, 0) - map_drop.get(i, 0)
		if acc > capacity:
			return False

	return True 

print(carPooling([[2,1,5],[3,3,7]], 4))