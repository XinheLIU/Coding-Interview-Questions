class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # BFS
        if not root:
            return []
        ret, q = [], [root]
        while len(q):
            # current level
            level = []
            for _ in range(len(q)):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ret.append(level)
        return ret
        
''' 
# DFS 
class Solution:
    def traverse(self, root, level, res):
        if not root:
            return
        # add one more empty layer
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        if root.left:
            self.traverse(root.left, level + 1, res)
        if root.right: 
            self.traverse(root.right, level + 1, res)
            
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # DFS
        res = []
        self.traverse(root, 0, res)
        return res
'''   