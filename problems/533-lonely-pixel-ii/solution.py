import collections
class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        m, n = len(picture), len(picture[0])
        rows, cols = [0] * m, [0] * n
        for x in range(m):
            for y in range(n):
                if picture[x][y] == 'B':
                    rows[x] += 1
                    cols[y] += 1

        sdict = collections.defaultdict(int)
        for x in picture:
            sdict[''.join(x)] += 1

        ans = 0
        for x in range(m):
            row = ''.join(picture[x])
            if sdict[row] != N:
                continue
            for y in range(n):
                if picture[x][y] == 'B':
                    if rows[x] == N:
                        if cols[y] == N:
                            ans += 1
        return ans