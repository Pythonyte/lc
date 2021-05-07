class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        def create_graph(prerequisites):
            graph = defaultdict(list)
            
            for v,u in prerequisites:
                graph[u].append(v)
            
                if v not in graph:
                    graph[v] = []
            return graph
        
        def compute_indigree(graph):
            in_digree = {u:False for u in graph}
            for u in graph:
                for v in graph[u]:
                    in_digree[v] += 1
            return in_digree
            
        def is_cycle(graph):
            in_digree = compute_indigree(graph)
            queue, count = [], 0
            
            for u, ingigree in in_digree.items():
                if ingigree == 0:
                    queue.append(u)
            while queue:
                node = queue.pop(0)
                count += 1
                for vertex in graph[node]:
                    in_digree[vertex] -= 1
                    if in_digree[vertex] == 0:
                        queue.append(vertex)
            if count == len(graph):
                return False
            
            return True 
                
        graph = create_graph(prerequisites)
        return not is_cycle(graph)
        
