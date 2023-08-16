from collections import defaultdict, deque

def topological_sort(graph):
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    queue = deque([node for node in graph if in_degree[node] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(result) == len(graph):
        return result
    else:
        return None  # Graph has a cycle, cannot perform topological sorting

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Topological Sorting:")
result = topological_sort(graph)

if result is not None:
    print(result)
else:
    print("Graph contains a cycle, cannot perform topological sorting.")

"""
Description:
    The topological_sort function takes a directed graph represented as an adjacency list.

    We create an in_degree dictionary to store the in-degree (number of incoming edges) for each node in the graph.

    We iterate through each node in the graph and its neighbors to calculate the in-degree for each node.

    We create a queue and enqueue all nodes with an in-degree of 0. These are the nodes that have no dependencies and can be placed at the beginning of the ordering.

    We create an empty result list to store the topological sorting result.

    While the queue is not empty, we dequeue a node, append it to the result, and then update the in-degree of its neighbors.

    If an updated neighbor has an in-degree of 0, we enqueue it.

    After the loop, if the length of the result list is equal to the number of nodes in the graph, then a valid topological ordering exists, and we return the result.

    If the length of the result list is less than the number of nodes, then the graph contains a cycle, and we return None.

    We provide an example graph as an adjacency list.

    Finally, we call the topological_sort function and print the result or a message indicating the presence of a cycle.

Conclusion:
    Topological Sorting is used when we have a set of tasks with dependencies, and we need to find a valid order in which to execute these tasks to satisfy the dependencies.

"""