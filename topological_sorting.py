# https://www.geeksforgeeks.org/topological-sorting/
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

    def topological_sorting_util(self, v, visited, stack):
        visited[v] = True
        for u in self.graph[v]:
            if visited[u] == False:
                self.topological_sorting_util(u, visited, stack)
        stack.append(v)

    def topological_sorting(self):
        visited = {v:False for v in self.graph}
        stack = []
        for v in self.graph:
            if visited[v] == False:
                self.topological_sorting_util(v, visited, stack)

        print(stack[::-1])


if __name__ == '__main__':
    # Driver Code
    g = Graph()
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    g.topological_sorting()