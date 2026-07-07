class Solution(object):
    def pathSum(self, nums):
        ret = 0
        values = {x // 10: x % 10 for x in nums}
        def dfs(node, running_sum = 0):
            nonlocal ret
            if node not in values: return
            running_sum += values[node]
            depth, pos = divmod(node, 10)
            left = (depth + 1) * 10 + 2 * pos - 1
            right = left + 1

            if left not in values and right not in values:
                ret += running_sum
            else:
                dfs(left, running_sum)
                dfs(right, running_sum)

        dfs(nums[0] // 10)
        return ret