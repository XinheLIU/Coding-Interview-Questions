#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, heights: List[int]) -> int:
        # decreasing stack
        stack = collections.deque()
        ret = 0
        for i, h in enumerate(heights):
            # decreasing stack
            while stack and h > heights[stack[-1]]:
                t = stack.pop()
                if not stack: continue
                ret += (min(h, heights[stack[-1]]) - heights[t]) * (i - stack[-1] - 1)
            stack.append(i)
        return ret 
# @lc code=end
'''
class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights: return 0
        ret = 0
        n = len(heights)
        left_max, right_max = heights[:], heights[:]
        
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i], right_max[i+1])
        
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], left_max[i])
            ret += min(left_max[i], right_max[i]) - heights[i]
            
        return ret
'''

'''
# two pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        ans = 0
        l, r = 0, len(height) - 1
        l_max, r_max = 0, 0
        while l < r:
            if height[l] < height[r]: 
                if height[l] > l_max:
                    l_max = height[l]
                else:
                    ans += l_max - height[l]
                l += 1
            else:                            
                if height[r] > r_max:
                    r_max = height[r]
                else:
                    ans += r_max - height[r]
                r -= 1
        return ans
'''
'''
class Solution:
    # decreasing stack
    def trap(self, height: List[int]) -> int:
        stack = collections.deque()
        i = 0
        ret = 0
        n = len(height)
        while i < n:
            # decreasing stack
            if not stack or height[stack[-1]] >= height[i]:
                stack.append(i)
                i += 1
            else:
                t = stack.pop()
                if not stack:
                    continue
                ret += (min(height[i], height[stack[-1]]) - height[t]) * (i - stack[-1] - 1)
        return ret
'''