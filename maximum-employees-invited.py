def addToGraph(graph, i, j):
	if i not in graph:
		graph[i] = set([j])
	else:
		graph[i].add(j)

	if j not in graph:
		graph[j] = set([i])
	else:
		graph[j].add(i)

def maximumInvitations(favorite):
	graph = {}
	res = 0
	for i in range(len(favorite)):
		addToGraph(graph, i, favorite[i])

	for num in graph:
		if len(graph[num]) >= 2:
			res += 1
	return res

# print(maximumInvitations([3,0,1,4,1]))
# print(maximumInvitations([1,2,0]))
print(maximumInvitations([2,2,1,2]))