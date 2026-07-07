class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        class unionfind:
            def __init__(self, n):
                self.count = n
                self.parent = [i for i in range(n)]
                self.rank = [1 for _ in range(n)]
               
            def get_count(self):
                return self.count
            
            def find(self, p):
                while p != self.parent[p]:
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p
            
            def union(self, p, q):
                p_root, q_root = self.find(p), self.find(q)
                if p_root == q_root:
                    return
                if self.rank[p_root] > self.rank[q_root]:
                    self.parent[q_root] = p_root
                elif self.rank[p_root] < self.rank[q_root]:
                    self.parent[p_root] = q_root
                else:
                    self.parent[q_root] = p_root
                    self.rank[p_root] += 1
                self.count -= 1

        disjoint_s = unionfind(n)
        for i, j in edges:
            disjoint_s.union(i, j)
        return disjoint_s.get_count()