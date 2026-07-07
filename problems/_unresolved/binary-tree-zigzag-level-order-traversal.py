class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        # use two stacks
        ret, s1, s2 = [], [], [] # or queue does not really matter
        s1.append(root)
        while len(s1) or len(s2):
            level = []
            while len(s1):
                cur = s1.pop()
                level.append(cur.val)
                if cur.left:
                    s2.append(cur.left)
                if cur.right:
                    s2.append(cur.right)
            if len(level): 
                ret.append(level)
            print(ret)
            level = []
            while len(s2):
                cur = s2.pop()
                level.append(cur.val)
                if cur.right:
                    s1.append(cur.right)
                if cur.left:
                    s1.append(cur.left)
            if len(level): 
                ret.append(level)
            print(ret)
        return ret
            