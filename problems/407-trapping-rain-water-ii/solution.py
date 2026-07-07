#
# @lc app=leetcode id=407 lang=python3
#
# [407] Trapping Rain Water II
#
# https://leetcode.com/problems/trapping-rain-water-ii/description/
#
# algorithms
# Hard (40.12%)
# Likes:    1031
# Dislikes: 26
# Total Accepted:    35.6K
# Total Submissions: 87.5K
# Testcase Example:  '[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]'
#
# Given an m x n matrix of positive integers representing the height of each
# unit cell in a 2D elevation map, compute the volume of water it is able to
# trap after raining.
# 
# 
# 
# Note:
# 
# Both m and n are less than 110. The height of each unit cell is greater than
# 0 and is less than 20,000.
# 
# 
# 
# Example:
# 
# 
# Given the following 3x6 height map:
# [
# ⁠ [1,4,3,1,3,2],
# ⁠ [3,2,1,3,2,4],
# ⁠ [2,3,3,2,3,1]
# ]
# 
# Return 4.
# 
# 
# 
# 
# The above image represents the elevation map
# [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.
# 
# 
# 
# 
# 
# After the rain, water is trapped between the blocks. The total volume of
# water trapped is 4.
# 
#

# @lc code=start
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap: return 0
        self.initialize(heightMap)
        water = 0

        while self.borders:
            height, x, y = heapq.heappop(self.borders)
            for x_, y_ in self.adjacent(x, y):
                water += max(0, height - heightMap[x_][y_])
                self.add(x_, y_, max(height, heightMap[x_][y_]))
        return water
    
    def initialize(self, heightMap):
        """add the borders to a min heap (priority queue)"""
        self.n = len(heightMap)
        self.m = len(heightMap[0])
        self.visited = set()
        self.borders = []

        for row in range(self.n):
            self.add(row, 0, heightMap[row][0])
            self.add(row, self.m - 1, heightMap[row][self.m - 1])
            
        for col in range(self.m):
            self.add(0, col, heightMap[0][col])
            self.add(self.n - 1, col, heightMap[self.n - 1][col])
    
    def add(self, x, y, height):
        """push to priority queue"""
        heapq.heappush(self.borders, (height, x, y))
        self.visited.add((x, y))
    
    def adjacent(self, x, y):
        for delta_x, delta_y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            x_ = x + delta_x
            y_ = y + delta_y
            if 0 <= x_ < self.n and 0 <= y_ < self.m and (x_, y_) not in self.visited:
                yield (x_, y_)
# @lc code=end

