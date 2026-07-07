#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = collections.defaultdict(list)
        for f, t in sorted(tickets)[::-1]:
            d[f] += [t]
        ret = []
        def dfs(f):
            while d[f]:
                dfs(d[f].pop())
            ret.append(f)
        dfs('JFK')
        return ret[::-1]
# @lc code=end

