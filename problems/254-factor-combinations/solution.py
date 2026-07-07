class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def dfs(n, ret, out, start = 2):
            while start * start <= n:
                if n % start == 0:
                    ret.append(out + [start, n // start])
                    dfs(n // start, ret, out + [start], start)
                start += 1
        ret = []
        dfs(n, ret, [])
        return ret


'''
class Solution(object):
  
  def dfs(self, n, subset, start):
    while start * start <= n:      
      if n % start == 0:
        self.result.append(subset + [start, n//start])
        self.dfs(n//start, subset + [start], start)        
      start += 1    
  
  def combinations(self, target):
    self.result = []
    self.dfs(target, [], 2)
    return self.result
''' 
"""
# TLE Solution
from math import sqrt
class Solution:
    def getFactors(self, n):
        def dfs(n, res, out, start):
            if n == 1 and len(out) > 1:
                res.append(out[:])
            for i in range(start, int(n) + 1):
                if n % i == 0:
                    out.append(i)
                    dfs(n // i, res, out, i)
                    out.pop()
        res = []
        dfs(n, res, [], 2)
        return res
"""