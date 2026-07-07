class DSU:
    def __init__(self, N):
        self.par = range(N)
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)

class Solution(object): # (NW) * min(N, W*W) complexity
    def numSimilarGroups(self, A):
        N, W = len(A), len(A[0])

        def similar(word1, word2):
            diff = 0
            for x, y in itertools.izip(word1, word2):
                if x != y:
                    diff += 1
            return diff <= 2

        dsu = DSU(N)

        if N < W*W: # If few words, then check for pairwise similarity: O(N^2 W)
            for (i1, word1), (i2, word2) in \
                    itertools.combinations(enumerate(A), 2):
                if similar(word1, word2):
                    dsu.union(i1, i2)

        else: # If short words, check all neighbors: O(N W^3)
            buckets = collections.defaultdict(set)
            for i, word in enumerate(A):
                L = list(word)
                for j0, j1 in itertools.combinations(xrange(W), 2):
                    L[j0], L[j1] = L[j1], L[j0]
                    buckets["".join(L)].add(i)
                    L[j0], L[j1] = L[j1], L[j0]

            for i1, word in enumerate(A):
                for i2 in buckets[word]:
                    dsu.union(i1, i2)

        return sum(dsu.par[x] == x for x in xrange(N))


'''
class Solution:
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        # 判断两个字符串是否是一个组
        def isSimilar(s1,s2):
            cnt = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    cnt += 1
                    if cnt > 2: return False
            return True

        # 标准的union find思路，也就是将所有在一个组内字符串用同一个字符串记录
        # 如 arts:arts, rats: arts, tars: arts, star: star
        d = {u:u for u in A}
        def find(u):
            if u != d[u]:
                d[u] = find(d[u])
            return d[u]

        #设初始组数为n，每找到一个该在同一组的总组数就减1
        self.n = len(A)
        def union(x,y):
            x,y = find(x),find(y)
            if x != y:
                d[y] = x
                self.n -= 1
                return True
            return False

        for x in range(len(A)):
            for y in range(x+1,len(A)):
                if isSimilar(A[x],A[y]): 
                    union(A[x],A[y])
        return self.n
'''


'''
class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        Graph = collections.defaultdict(list)
        # 判断两个字符串是否是在一个组
        def isSimilar(x,y):
            res = 0
            for i in range(len(x)):
                if x[i] != y[i]:
                    res += 1
                    if res > 2: return False
            return res == 2

        # 构建图，O(m*n^2) time
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                if isSimilar(A[i],A[j]):
                    Graph[i].append(j)
                    Graph[j].append(i)

        # 用一个数组判断节点是否已被访问
        visited = [0] * len(A)
        def dfs(u):
            visited[u] = 1
            for v in Graph[u]:
                if visited[v]: continue
                dfs(v)

        res = 0
        for i in range(len(A)):
            if visited[i]: continue
            # 一次dfs得到一个连通分量
            dfs(i)
            res += 1
        return res
'''