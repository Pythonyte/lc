https://www.geeksforgeeks.org/detect-cycle-in-a-graph/

# Python program to detect cycle
# in a graph

from collections import defaultdict


# https://www.geeksforgeeks.org/topological-sorting/
# Python program to print DFS traversal for complete graph
from collections import defaultdict


# This class represents a directed graph using adjacency
# list representation
from collections import defaultdict, deque
class Graph:
    def __init__(self):
       self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)   

    def detect_cycle_in_undirected_graph_util(self, visited, parent=None, vertex=None):
        visited[vertex] = True
        for v in self.graph[vertex]:
            if visited[v] == False:
                if self.detect_cycle_in_undirected_graph_util(visited, parent=vertex, vertex=v):
                    return True
            elif parent != v:
                return True

    def detect_cycle_in_undirected_graph(self):
        visited = {u:False for u in self.graph}
        for u in self.graph:
            if visited[u] == False:
                if self.detect_cycle_in_undirected_graph_util(visited, parent=-1, vertex=u):
                    return True
        return False


if __name__ == '__main__':
    # Driver Code
    g = Graph()
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    #print(g.topological_sorting_dfs_approach())
    # g.addEdge(1, 3)
    #print(g.topological_sorting_dfs_approach())
    #print(g.topological_sorting_indigree_approach())
    print(g.detect_cycle_in_undirected_graph())


#####################################################################################################################
#####################################################################################################################
#####################################################################################################################


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):
        print(v, visited, recStack)
        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True

        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True

        # The node needs to be poped from
        # recursion stack before function ends
        recStack[v] = False
        return False

    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
if g.isCyclic() == 1:
    print("Graph has a cycle")
else:
    print("Graph has no cycle")
