class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        # write your code here
        moves, n, s = [], len(s), list(s)
        for i in xrange(n - 1):
            if s[i] == s[i + 1] == '+': 
                s[i] = s[i + 1] = '-'
                moves += ''.join(s),
                s[i] = s[i + 1] = '+' 
        return moves