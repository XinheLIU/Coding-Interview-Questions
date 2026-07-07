#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (33.95%)
# Likes:    1858
# Dislikes: 833
# Total Accepted:    308.5K
# Total Submissions: 906.4K
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
# 
# Example 1:
# 
# 
# Input: num1 = "2", num2 = "3"
# Output: "6"
# 
# Example 2:
# 
# 
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# 
# 
# Note:
# 
# 
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = [0] * (len(num1) + len(num2))
        i = len(product) - 1
        for n1 in reversed(num1):
            j = i
            for n2 in reversed(num2):
                product[j] += int(n1) * int(n2)
                product[j-1] += product[j] // 10
                product[j] %= 10
                j -= 1
            i-= 1
        # count digits
        pt = 0
        while pt < len(product) - 1 and product[pt] == 0:
            pt += 1
        return ''.join(map(str, product[pt:]))
# @lc code=end