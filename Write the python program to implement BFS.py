from collections import deque

def bfs(graph, start_node):
    """
    Implements the Breadth-First Search (BFS) algorithm.

    Args:
        graph (dict): An adjacency list representation of the graph.
                      Example: {
                          'A': ['B', 'C'],
                          'B': ['D', 'E'],
                          'C': ['F'],
                          'D': [],
                          'E': ['F'],
                          'F': []
                      }
        start_node: The node from which to start the BFS traversal.

    Returns:
        list: A list containing the nodes in the order they were visited during BFS.
    """
    if start_node not in graph:
        print(f"Error: Start node '{start_node}' not found in the graph.")
        return []

    visited = set()  # To keep track of visited nodes
    queue = deque()  # Use a deque for efficient appends and pops from both ends

    # Add the start node to the queue and mark it as visited
    queue.append(start_node)
    visited.add(start_node)

    traversal_order = []  # To store the order of visited nodes

    while queue:
        # Dequeue a node from the front of the queue
        current_node = queue.popleft()
        traversal_order.append(current_node)

        # Explore all unvisited neighbors of the current node
        for neighbor in graph.get(current_node, []): # .get handles nodes with no neighbors
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return traversal_order

# Example Usage:

# Define a sample graph using an adjacency list
sample_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

print("BFS Traversal starting from 'A':")
bfs_result = bfs(sample_graph, 'A')
print(bfs_result) # Expected: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

print("\nBFS Traversal starting from 'C':")
bfs_result_c = bfs(sample_graph, 'C')
print(bfs_result_c) # Expected: ['C', 'F', 'G']

print("\nBFS Traversal for a disconnected graph component (starting from 'Z' not in graph):")
bfs_result_invalid = bfs(sample_graph, 'Z')
print(bfs_result_invalid) # Expected: Error message and []
