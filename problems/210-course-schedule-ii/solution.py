#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = {i:[] for i in range(numCourses)}
        degrees = [0 for _ in range(numCourses)]
        # indegree
        for i, j in prerequisites:
            edges[j].append(i)
            degrees[i] += 1
        
        q, count, ret = collections.deque(), 0, []

        q = collections.deque([i for i in range(numCourses) if degrees[i] == 0])

        while q:
            node = q.popleft()
            count += 1
            ret.append(node)
            for x in edges[node]: 
                degrees[x] -= 1
                if degrees[x] == 0:
                    q.append(x)
        
        return ret if count == numCourses else []
        
# @lc code=end

