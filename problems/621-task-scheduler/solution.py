#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
       cnt = collections.Counter(tasks)
       counts = list(cnt.values())
       longest = max(counts) 
       return max((longest - 1)  * (n + 1) + counts.count(longest), len(tasks))
# @lc code=end

'''
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        f= [0] * 26
        for t in tasks:
            f[ord(t) - ord('A')] += 1
        
        f.sort()

        # max frequency
        f_max = f.pop()
        idle_time = (f_max - 1) * n
        
        while f and idle_time > 0:
            idle_time -= min(f_max - 1, f.pop())
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)
'''