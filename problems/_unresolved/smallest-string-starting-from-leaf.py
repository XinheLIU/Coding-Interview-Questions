class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def dfs(root, path, res):
            if not root.left and not root.right:
                res.append(chr(root.val + ord('a')) + path)
                return
            if root.left:
                dfs(root.left, chr(root.val + ord('a')) + path, res)
            if root.right:
                dfs(root.right, chr(root.val + ord('a')) + path, res)
        res = []
        if not root:
            return res
        dfs(root, "", res)
        return sorted(res)[0]

"""
class Solution(object):
    def smallestFromLeaf(self, root):
        q = collections.deque()
        q.append((root, ""))
        res = []
        while q:
            node, path = q.popleft()
            if not node.left and not node.right:
                res.append(chr(node.val + ord('a')) + path)
                continue
            if node.left:
                q.append((node.left, chr(node.val + ord('a')) + path))
            if node.right:
                q.append((node.right, chr(node.val + ord('a')) + path))
        res.sort()
        return res[0]
"""
"""
class Solution(object):
    def smallestFromLeaf(self, root):
        self.ans = "~"

        def dfs(node, A):
            if node:
                A.append(chr(node.val + ord('a')))
                if not node.left and not node.right:
                    self.ans = min(self.ans, "".join(reversed(A)))

                dfs(node.left, A)
                dfs(node.right, A)
                A.pop()

        dfs(root, [])
        return self.ans
"""