import itertools

def tsp(graph):
    n = len(graph)
    return min(sum(graph[i][j] for i, j in zip(path, path[1:] + (path[0],))) for path in itertools.permutations(range(n)))

# Example usage
graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
print(tsp(graph))
