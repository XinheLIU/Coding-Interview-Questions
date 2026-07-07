class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # tarjan algorithm
        visited = set()
        low = [9999999] * n
        discover = [999999] * n
        parent = [-1] * n
        graph = defaultdict(list)
        time = 0
        ret = []
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(u):
            nonlocal time
            visited.add(u)
            discover[u] = time
            low[u] = time
            time += 1
 
            for v in graph[u]:
                if v not in visited:
                    parent[v] = u
                    dfs(v)
                    low[u] = min(low[u], low[v])
 
                    if low[v] > discover[u]:
                        ret.append([u, v])
                elif v != parent[u]:
                    low[u] = min(low[u], discover[v])
                
        for i in range(n):
            if i not in visited:
                dfs(i)
        return ret