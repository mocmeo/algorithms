class Graph:
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g

    def isSafe(self, i, j, visited, color):
        return (i >= 0 and i < self.ROW and
                j >= 0 and j < self.COL and
                not visited[i][j] and self.graph[i][j] == color)

    def DFS(self, i, j, visited, newColor):
        rowDir = [-1, 1, 0, 0]
        colDir = [0, 0, 1, -1]
        visited[i][j] = True

        oldColor = self.graph[i][j]
        self.graph[i][j] = newColor

        for k in range(4):
            if self.isSafe(i + rowDir[k], j + colDir[k], visited, oldColor):
                self.DFS(i + rowDir[k], j + colDir[k], visited, newColor)


def floodFill(image, sr, sc, newColor):
    row = len(image)
    col = len(image[0])
    g = Graph(row, col, image)

    visited = [[False]*g.COL for i in range(g.ROW)]
    g.DFS(sr, sc, visited, newColor)
    return g.graph


print(floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
