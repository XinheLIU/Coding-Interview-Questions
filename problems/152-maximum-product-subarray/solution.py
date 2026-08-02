class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Maximum Product Subarray: track both max AND min at each position
        # Why? A negative number flips the sign — today's min becomes tomorrow's max
        # when multiplied by another negative.
        #
        # State: dp_max[i] = max product ending at i
        #        dp_min[i] = min product ending at i (for negative flips)
        # Transition: dp_max[i] = max(nums[i], dp_max[i-1]*nums[i], dp_min[i-1]*nums[i])
        #             dp_min[i] = min(nums[i], dp_max[i-1]*nums[i], dp_min[i-1]*nums[i])
        #
        # Space-optimized: rolling array [0] and [1] alternating as i % 2
        ret = nums[0] if nums else 0
        dp_max, dp_min = [0] * 2, [0] * 2
        dp_max[0], dp_min[0] = nums[0], nums[0]

        for i in range(1, len(nums)):
            x, y = i % 2, (i-1) % 2  # current slot, previous slot
            # Either start fresh from nums[i], or extend previous max/min
            # Must consider both because a negative nums[i] makes min → max
            dp_max[x] = max(nums[i], dp_max[y] * nums[i], dp_min[y] * nums[i])
            dp_min[x] = min(nums[i], dp_max[y] * nums[i], dp_min[y] * nums[i])
            ret = max(ret, dp_max[x])
        return ret