class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        m, n = len(picture), len(picture[0])
        rows, cols = [0] * m, [0] * n
        for x in range(m):
            for y in range(n):
                if picture[x][y] == 'B':
                    rows[x] += 1
                    cols[y] += 1
        ans = 0
        for x in range(m):
            for y in range(n):
                if picture[x][y] == 'B':
                    if rows[x] == 1:
                        if cols[y] == 1:
                            ans += 1
        return ans
"""
class Solution(object):
    def findLonelyPixel(self, picture):
        return sum(col.count('B') == 1 == picture[col.index('B')].count('B') \
               for col in zip(*picture))
"""