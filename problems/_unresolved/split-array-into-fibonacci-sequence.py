class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        def dfs(S, start, out, res):
            if len(res): return # only one ans
            if len(out) >= 3 and out[-1] != out[-2] + out[-3]: 
                return
            if start >= len(S) and len(out) >= 3: 
                res.extend(out)
                return
            for i in range(start, len(S)):
                cur = S[start:i+1]
                if int(cur) >= 2**31: 
                    continue
                if cur[0] == '0' and len(cur) != 1:
                    continue              
                out.append(int(cur))
                dfs(S, i + 1, out, res)
                out.pop()
        res = []
        dfs(S, 0, [], res)
        return res