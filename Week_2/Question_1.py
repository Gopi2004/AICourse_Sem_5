"""
    You are given with a connected and undirected simple graph
    with N vertices and M edges. Your task is to direct each edge in one of
    two possible directions in such a way that the indegrees of all vertices of
    the resulting graph are even. The indegree of a vertex is the number of
    edges directed to that vertex from another vertex. Find one possible way
    to direct them or determine that it is impossible under the given
    conditions. The graph on the input is connected, does not contain multiple
    edges or self-loops.
    For each test case 
    (Output):
     If a valid way to direct the edges does not exist, print a single line
    containing one integer -1.
     Otherwise, print a single line containing M space-separated integers.
    For each valid i, the i-th of these integers should be 0 if edge i is
    directed from u i  to v i or 1 if it is directed from v i to u i .
"""

def solve(N, M, edges):
    in_degrees = [0] * (N + 1)
    out_edges = [[] for _ in range(N + 1)]
    
    for u, v in edges:
        out_edges[u].append(v)
        out_edges[v].append(u)
        in_degrees[u] += 1
        in_degrees[v] += 1
    
    odd_degrees = sum(1 for degree in in_degrees if degree % 2 == 1)
    
    if odd_degrees == 0 or odd_degrees == 2:
        eulerian_circuit = []
        stack = [1]  # Start traversal from vertex 1
        while stack:
            u = stack[-1]
            if out_edges[u]:
                v = out_edges[u].pop()
                stack.append(v)
                eulerian_circuit.append((u, v))
            else:
                stack.pop()
        
        if len(eulerian_circuit) != M:
            return -1
        else:
            directions = [0 if (u, v) in eulerian_circuit else 1 for u, v in edges]
            return directions
    else:
        return -1

# Example usage
N = 4
M = 3
edges = [(1, 2), (2, 3), (3, 4)]
result = solve(N, M, edges)

if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))
