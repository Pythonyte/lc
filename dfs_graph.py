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
        if v not in self.graph:
            self.graph[v] = []
        # A function used by DFS

    def DFSUtil(self, v, visited):
        # efaultdict(<class 'list'>, {0: [1, 2], 1: [2], 2: [0, 3], 3: [3], 4: [5, 6]})
        # Mark the current node as visited and print it
        visited[v] = True
        print(v)
        # Recur for all the vertices adjacent to
        # this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

                # The function to do DFS traversal. It uses

    # recursive DFSUtil()
    def DFS(self):
        visited = {v:False for v in self.graph}

        # Call the recursive helper function to print
        # DFS traversal starting from all vertices one
        # by one
        print(self.graph)
        for i in self.graph:
            if visited[i] == False:
                print(i, "=====")
                self.DFSUtil(i, visited)

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

print("Following is Depth First Traversal")
g.DFS()
