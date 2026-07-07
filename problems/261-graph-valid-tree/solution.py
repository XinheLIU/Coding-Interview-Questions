class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        root = [i for i in range(n)]
        size = n
        
        def find(node):
            nonlocal size, root
            path = []
            while node != root[node]:
                path.append(node)
                node = root[node]
            for n in path:
                root[n] = node
            return node
        
        def union(a, b):
            nonlocal size, root
            root_a, root_b = find(a), find(b)
            if root_a != root_b:
                size -= 1
                root[root_b] = root_a
        
        for a, b in edges:
            union(a, b)

        return size == 1

'''

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set([0])
        q = collections.deque([0])
        while q:
            cur = q.popleft()
            for node in graph[cur]:
                if node not in visited:
                    visited.add(node)
                    q.append(node)
        return len(visited) == n
'''