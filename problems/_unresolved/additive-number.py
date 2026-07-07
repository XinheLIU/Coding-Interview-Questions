class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(num, out):
            if len(out) >= 3 and out[-1] != out[-2] + out[-3]:
                return False
            if not len(num) and len(out) >= 3:
                return True
            for i in range(len(num)):
                cur = num[:i+1]
                if (cur[0] == '0' and len(cur) != 1):
                    continue     
                if dfs(num[i+1:], out + [int(cur)]):
                    return True
            return False
        return dfs(num, [])