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
    
        def compute_in_digree(self):
        in_digree = {v:0 for v in self.graph}
        for u in self.graph:
            for v in self.graph[u]:
                in_digree[v] += 1
        return in_digree

    # https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/
    # This soln will do both (1. detect a cycle, 2. Topological sorting)
    def topological_sorting_kahns(self):
        in_digree = self.compute_in_digree()
        sorted_vertices = []
        queue = []
        for v in self.graph:
            if in_digree[v] == 0:
                queue.append(v)
        print(in_digree, self.graph)
        count_nodes = 0
        while queue:
            node = queue.pop(0)
            sorted_vertices.append(node)
            for v in self.graph[node]:
                in_digree[v] -= 1
                if in_digree[v] == 0:
                    queue.append(v)
            # print(in_digree)
            count_nodes += 1

        print(in_digree)
        # print(sorted_vertices, count_nodes)
        if count_nodes == len(self.graph):
            return sorted_vertices
        else:
            print("Graph has Cycle")


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
