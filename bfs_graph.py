# Python program to print DFS traversal for complete graph
from collections import defaultdict


# This class represents a directed graph using adjacency
# list representation
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        # This is used to create a key for vertex which has so outgoing edge
        if v not in self.graph:
            self.graph[v] = []


    def BFSUtil(self, v, visited):
        from collections import deque
        # Mark the current node as visited and print it
        q = deque([v])
        visited[v] = True
        # Recur for all the vertices adjacent to
        # this vertex
        while q:
            vertex = q.popleft()
            print(vertex)
            for i in self.graph[vertex]:
                if visited[i] == False:
                    q.append(i)
                    visited[i] = True

    def BFS(self):
        visited = {v:False for v in self.graph}

        # Call the recursive helper function to print
        # DFS traversal starting from all vertices one
        # by one
        print(self.graph)
        for i in self.graph:
            if visited[i] == False:
                print("=====")
                self.BFSUtil(i, visited)

# Driver code
# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.addEdge(4, 5)
g.addEdge(4, 6)
g.addEdge(4, 7)
g.addEdge(5, 8)

print("Following is Depth First Traversal")
g.BFS()
