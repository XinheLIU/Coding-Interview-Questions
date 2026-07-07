class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return n
        
        list_dict = collections.defaultdict(list)
        for i, j in edges:
            list_dict[i].append(j)
            list_dict[j].append(i)
        
        def bfs(node, visited):
            queue = [node]
            while queue:
                nd = queue.pop(0)
                for neighbor in list_dict[nd]:
                    if neighbor not in visited:
                        visited.append(neighbor)
                        queue.append(neighbor)
            return visited
            
        def find_root(visited):
            for i in range(n):
                if i not in visited:
                    return i
            return -1
        
        visited = []
        count = 0
        for i in range(n):
            node = find_root(visited)
            if node != -1:
                count+=1
                visited.append(node)
                visited = bfs(node, visited)
            else:
                return count