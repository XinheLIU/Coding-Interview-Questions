#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(s, path, ret):
            if len(s) > (4 - len(path)) * 3:
                return
            if not s and len(path) == 4:
                ret.append('.'.join(path))
                return
            for i in range(min(3, len(s))):
                curr = s[:i+1]
                if (curr[0] == '0' and len(curr) >= 2) or int(curr) > 255:
                    continue
                dfs(s[i+1:], path + [s[:i+1]], ret)
        ret = []
        dfs(s, [], ret)
        return ret
# @lc code=end

