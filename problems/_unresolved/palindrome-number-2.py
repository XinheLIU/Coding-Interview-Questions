class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x // 10 == 0):
            return True
       
        #if the last digit is 0, return false
        if(x % 10 == 0):
            return False
        # revert a half
        reverse = 0   
        while(reverse < x):
            reverse *= 10
            reverse += x % 10
            x //= 10
        # if total digit is odd, the last digit should be on reverse, otherwise it is x
        if(reverse == x or reverse// 10 == x):
            return True
        return False
