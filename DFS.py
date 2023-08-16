def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")  # Print the visited node
        visited.add(node)     # Mark the node as visited
        
        # Recur for all the neighbors of the node
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
visited_nodes = set()

print("Depth-First Traversal starting from node", start_node)
dfs(graph, start_node, visited_nodes)

"""
Description:
    The dfs function takes three arguments: the graph (represented as an adjacency list), the current node, and the visited set that keeps track of visited nodes.

    We start by checking if the current node is not in the visited set. If it's not visited, we print the node and mark it as visited by adding it to the visited set.

    Next, we enter a loop that iterates over all the neighbors of the current node.

    For each neighbor, we call the dfs function recursively with the neighbor node. This allows us to explore deeper into the graph.

    Since we check for visited nodes before exploring, we ensure that each node is visited only once.

    We provide an example graph as an adjacency list.

    Finally, we call the dfs function with the starting node and an empty visited_nodes set. The DFS traversal proceeds recursively, exploring as deeply as possible along each branch before backtracking.

Conclusion:

    Depth-First Search explores the graph by going as deep as possible along each branch before exploring other branches. This can lead to a deeper exploration of individual branches before moving on to other parts of the graph.
"""