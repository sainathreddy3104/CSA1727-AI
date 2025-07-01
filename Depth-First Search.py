def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    
    traversal_order = []
    
    # Define the recursive DFS helper function
    def dfs_recursive(node):
        # Mark the current node as visited and add to traversal order
        visited.add(node)
        traversal_order.append(node)
        
        # Recursively visit all unvisited neighbors
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_recursive(neighbor)
    
    # Start DFS from the given start node
    if start_node not in graph:
        print(f"Error: Start node '{start_node}' not found in the graph.")
        return []
    
    dfs_recursive(start_node)
    return traversal_order

# Example Usage:
if __name__ == "__main__":
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

    print("DFS Traversal starting from 'A':")
    dfs_result = dfs(sample_graph, 'A')
    print(dfs_result)  # Expected: ['A', 'B', 'D', 'E', 'H', 'C', 'F', 'G']
