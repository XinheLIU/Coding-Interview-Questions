class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or not len(digits):
            return []
        kvmaps = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        def dfs(digits, kvmaps, index, out, res):
            if len(out) >= len(digits):
                res.append(out)
                return
            for i in kvmaps[digits[index]]:
                dfs(digits, kvmaps, index + 1, out + i, res)
        res = []
        dfs(digits, kvmaps, 0, "", res)
        return res