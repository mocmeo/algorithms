import collections

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

def bfs(graph, node):
  visited, queue = set(), collections.deque([node])
  visited.add(node)

  while queue:
    s = queue.popleft() 
    print(s)

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.add(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(graph, 'A')