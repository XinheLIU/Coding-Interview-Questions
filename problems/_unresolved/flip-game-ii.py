class Solution:
    """
    @param s: the given string
    @return: if the starting player can guarantee a win
    """
    class Solution:
    def canWin(self, s: str) -> bool:
        for i in range(1, len(s)):
            if s[i-1:i+1] == "++" and not self.canWin(s[:i-1] + "--" + s[i+1:]):
                return True
        return False

'''
    def canWin(self, s):
        # write your code here
        return any(not self.canWin(s[:i]+"--"+s[i+2:]) for i in range(len(s)-1) if s[i:i+2] == "++")
'''