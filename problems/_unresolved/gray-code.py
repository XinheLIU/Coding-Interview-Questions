class Solution:
    def grayCode(self, n: int) -> List[int]:
        def DFS(n, ans, num, level, targetLevel):
            if num in ans:
                return
            ans.append(num)
            if level == targetLevel:
                return
            for i in range(0, n):
                DFS(n, ans, num ^ (1 << i), level+1, targetLevel)  # flip one bit at a time  
        ans = []
        DFS(n, ans, 0, 1, 2**n)   # Start with number = 0 (000), level = 1, (level is the # of running here)
        return ans