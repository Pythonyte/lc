class Solution:
# https://leetcode.com/problems/kill-process/
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
    # Approach 1
#         def helper(kill):
            
#             nonlocal output
#             if kill in output: return
            
#             output.append(kill)
#             for i, parent in enumerate(ppid):
#                 if parent == kill:
#                    helper(pid[i])             
            
#         output = []
#         if kill not in pid:
#             return []
        
#         helper(kill)
#         return output
        
        from collections import deque, defaultdict
        
        def create_graph(pid, ppid):
            graph = defaultdict(list)
            for i, u in enumerate(ppid):
                v = pid[i]
                graph[u].append(v)
                if v not in graph:
                    graph[v] = []
            return graph
        
        def bfs(graph, root):
            output = []
            if root not in graph: return []
            
            queue = deque([root])
            while queue:
                u = queue.popleft()
                output.append(u)
                for v in graph[u]:
                    queue.append(v)
                
            return output
        
        graph = create_graph(pid, ppid)
        print(graph)
        return bfs(graph, kill)
