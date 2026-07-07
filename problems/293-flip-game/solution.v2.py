class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        ret = []
        for i in range(1, len(s)):
            if s[i] == s[i-1] == "+":
                ret.append(s[:i-1] + "--" + s[i+1:])
        return ret