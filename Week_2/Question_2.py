"""
    There are a total n tasks you must pick, labelled from 0 to n-1. Some
    tasks may have pre-requisites and for example to pick task 0 you have to
    first pick task 1, which is expressed as a pair [0, 1].
    Write a function
    bool canFinish(int tasks, int [][] prerequsites)
    that return true or false if it is possible for you to finish all tasks or not.

    Input: tasks = 2, pre-requsites = [ [0,1], [1,0] ]
    Output: False
    Input: tasks=3, pre-requsites = [ [1,0], [0,2] ]
    Output: True

"""

from collections import defaultdict, deque

def canFinish(tasks, prerequisites):
    # Create a graph representation with adjacency lists
    graph = defaultdict(list)
    in_degree = [0] * tasks
    
    # Build the graph and calculate in-degrees
    for prerequisite in prerequisites:
        course, prerequisite_for = prerequisite
        graph[prerequisite_for].append(course)
        in_degree[course] += 1
    
    # Create a queue for BFS
    queue = deque()
    
    # Initialize the queue with tasks having in-degree 0
    for task in range(tasks):
        if in_degree[task] == 0:
            queue.append(task)
    
    # Perform topological sort using BFS
    while queue:
        task = queue.popleft()
        tasks -= 1
        
        for next_task in graph[task]:
            in_degree[next_task] -= 1
            if in_degree[next_task] == 0:
                queue.append(next_task)
    
    # If all tasks were processed, return True; otherwise, return False
    return tasks == 0

# Test cases
print(canFinish(2, [[0, 1], [1, 0]]))  # Output: False
print(canFinish(3, [[1, 0], [0, 2]]))  # Output: True
