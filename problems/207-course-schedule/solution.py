#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = {i: [] for i in range(numCourses)}
        degrees = [0 for _ in range(numCourses)]
        for i, j in prerequisites:
            edges[j].append(i)
            degrees[i] += 1
        
        q, count = collections.deque(), 0
        
        q = collections.deque([i for i in range(numCourses) if degrees[i] == 0])
        
        while q:
            node = q.popleft()
            count += 1
            for x in edges[node]:
                degrees[x] -= 1
                if degrees[x] == 0:
                    q.append(x)
            
        return count == numCourses
# @lc code=end

