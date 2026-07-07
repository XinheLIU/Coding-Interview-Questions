#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#
# https://leetcode.com/problems/k-closest-points-to-origin/description/
#
# algorithms
# Medium (63.84%)
# Likes:    2126
# Dislikes: 120
# Total Accepted:    332.7K
# Total Submissions: 519.7K
# Testcase Example:  '[[1,3],[-2,2]]\n1'
#
# We have a list of points on the plane.  Find the K closest points to the
# origin (0, 0).
# 
# (Here, the distance between two points on a plane is the Euclidean
# distance.)
# 
# You may return the answer in any order.  The answer is guaranteed to be
# unique (except for the order that it is in.)
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation: 
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just
# [[-2,2]].
# 
# 
# 
# Example 2:
# 
# 
# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000
# 
# 
# 
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = lambda i: points[i][0]**2 + points[i][1]**2
        def sort(l, r, K):
            if l >= r: return
            pivot_pos = partition(l, r)
            if K < pivot_pos - l + 1:
                sort(l, pivot_pos - 1, K)
            elif K > pivot_pos - l + 1:
                sort(pivot_pos + 1, r, K - (pivot_pos - l + 1))

        def partition(l, r):
            rand = random.randint(l, r)
            points[rand], points[r] = points[r], points[rand]
            pivot = dist(r)
            i = l - 1
            for j in range(l, r):
                if dist(j) < pivot:
                    i += 1
                    points[i], points[j] = points[j], points[i]
            points[r], points[i+1] = points[i+1], points[r]
            return i + 1
        sort(0, len(points) - 1, K)
        return points[:K]   
# @lc code=end

