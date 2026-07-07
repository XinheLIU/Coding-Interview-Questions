#
# @lc app=leetcode id=547 lang=python3
#
# [547] Friend Circles
#

# @lc code=start
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        # union find
        def parent(p,i):
            root = i
            while p[root] != root:
                root = p[root]
            while p[i] != i:
                x = i; i = p[i]; p[x] = root
            return root

        def union(p, i, j):
            p1, p2 = parent(p, i), parent(p, j)
            p[p2] = p1
        
        n = len(M)
        p = [i for i in range(n)]
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    union(p, i, j)
        
        return(len(set([parent(p, i) for i in range(n)])))
        
# @lc code=end
'''
# BFS
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # use the fact matrix is symetric 
        visited = [False for _ in range(len(M))]
        q = collections.deque()
        ret = 0
        for i in range(len(M)):
            if not visited[i]:
                q.append(i)
                while q:
                    s = q.popleft()
                    visited[s] = True
                    for j in range(len(M[s])):
                        if M[s][j] and not visited[j]:
                            q.append(j)
                ret += 1
        return ret
'''

'''
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def dfs(M, visited, i):
            for j in range(len(M[i])):
                if not visited[j] and M[i][j]:
                    visited[j] = True
                    dfs(M, visited, j)
        
        visited = [False for _ in range(len(M))]
        ret = 0
        for i in range(len(M)):
            if not visited[i]:
                dfs(M, visited, i)
                ret += 1
        return ret
'''
