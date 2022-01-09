import collections

def bfs(arr, mapper, node, res):
	visited, queue = set(), collections.deque([node])
	visited.add(node)

	while queue:
		s = queue.popleft()

		vertices = mapper[arr[s]]
		if s + 1 < len(arr):
			vertices.append(s+1)
		if s - 1 >= 0:
			vertices.append(s-1)

		mapper[arr[s]] = []

		for neighbor in vertices:
			if neighbor not in visited and neighbor != s:
				if res[s] + 1 < res[neighbor]:
					res[neighbor] = res[s] + 1
					visited.add(neighbor)
					queue.append(neighbor)


def minJumps(arr):
	mapper = {}
	graph = {}
	res = [len(arr)+1]*len(arr)
	res[0] = 0

	for i in range(len(arr)):
		node = arr[i]
		if node in mapper:
			mapper[node].append(i)
		else:
			mapper[node] = [i]

	bfs(arr, mapper, 0, res)
	return res[-1]


# print(minJumps([100,-23,-23,404,100,23,23,23,3,404]))
# print(minJumps([7,6,9,6,9,6,9,7]))
print(minJumps([7,7,7,7,7,7,10]))


  