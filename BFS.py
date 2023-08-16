from collections import deque

def bfs(graph, start):
    # Create a queue for BFS and enqueue the starting node
    queue = deque([start])
    
    # Create a set to keep track of visited nodes
    visited = set([start])
    
    while queue:
        # Dequeue a node from the front of the queue
        node = queue.popleft()
        
        print(node, end=" ")  # Print the visited node
        
        # Visit all neighbors of the dequeued node
        for neighbor in graph[node]:
            if neighbor not in visited:
                # Enqueue the neighbor if it hasn't been visited yet
                queue.append(neighbor)
                visited.add(neighbor)

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
print("Breadth-First Traversal starting from node", start_node)
bfs(graph, start_node)

""" 
Description:
    We start by importing the deque class from the collections module. A deque is a double-ended queue that we will use for implementing the BFS queue.

    The bfs function takes two arguments: the graph (represented as an adjacency list) and the start node from which we want to begin the traversal.

    We create a queue (deque) and enqueue the start node.

    We also create a visited set to keep track of nodes we have already visited.

    The main loop continues until the queue is empty.

    Inside the loop, we dequeue a node from the front of the queue and print it. This simulates the visiting of the node.

    We then iterate through the neighbors of the current node. If a neighbor has not been visited yet, we enqueue it and mark it as visited.

    The loop continues until all nodes have been visited.

    We provide an example graph as an adjacency list.

    Finally, we call the bfs function with the starting node and print the breadth-first traversal.

    This implementation ensures that nodes are visited in the order they are encountered at each depth level, which is the fundamental characteristic of Breadth-First Search.
"""