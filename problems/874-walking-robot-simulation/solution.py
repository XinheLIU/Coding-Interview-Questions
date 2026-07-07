#
# @lc app=leetcode id=874 lang=python3
#
# [874] Walking Robot Simulation
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = ((0,1), (1, 0), (0, -1), (-1, 0))
        x, y = 0, 0
        di = 0
        obstacles = set(map(tuple, obstacles))
        ret = 0
        for cmd in commands:
            if cmd == -2:
                di = (di - 1) % 4
            elif cmd == -1:
                di = (di + 1) % 4
            else:
                for _ in range(cmd):
                    nx, ny = x + directions[di][0], y + directions[di][1]
                    if (nx, ny) not in obstacles:
                        x, y = nx, ny
                        ret = max(ret, x*x + y*y)
        return ret
# @lc code=end

