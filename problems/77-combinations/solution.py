class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(ret, out, start, n, k):
            if len(out) == k: 
                ret.append(out)
                return
            for i in range(start, n + 1):
                dfs(ret, out + [i], i + 1, n, k)
        ret = []
        dfs(ret, [], 1, n, k)
        return ret

'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(n, k, start, out, res):
            if len(out) == k:
                res.append(out[:])
                return
            for i in range(start, n+1):
                out.append(i)
                dfs(n, k,  i + 1, out, res)
                out.pop()
        res = []
        dfs(n, k, 1, [], res)
        return res
'''

"""
class Solution:
    def combine(self, n: 'int', k: 'int') -> 'List[List[int]]':   
        # write your code here  
        self.res = []
        self.dfs(n, k, 1, [])       
        return self.res

    def dfs(self, n, k, m, tmp):
        if k == len(tmp):
            self.res.append(tmp[:])
            return
        if len(tmp) > k:
            return
        for i in range(m, n+1):            
            tmp.append(i)            
            self.dfs(n, k, i+1, tmp)            
            tmp.pop()
"""
        