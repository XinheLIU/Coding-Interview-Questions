class Solution:
    def boundaryOfBinaryTree(self, root):
        self.ans = []
        if root == None:
            return self.ans
        self.ans.append(root.val)
        if root.left == None and root.right == None:
            return self.ans
        self.dfsLeft(root.left)
        self.dfsLeaf(root)
        self.dfsRight(root.right)
        return self.ans
    
    def dfsLeft(self, rt):
        if rt == None or (rt.left == None and rt.right == None):
            return
        self.ans.append(rt.val)
        if rt.left != None:
            self.dfsLeft(rt.left)
        else:
            self.dfsLeft(rt.right)
        
    def dfsLeaf(self, rt):
        if rt == None:
            return 
        if rt.left == None and rt.right == None:
            self.ans.append(rt.val)
            return
        self.dfsLeaf(rt.left)
        self.dfsLeaf(rt.right)
    
    def dfsRight(self, rt):
        if rt == None or (rt.left == None and rt.right == None):
            return
        if rt.right != None:
            self.dfsRight(rt.right)
        else:
            self.dfsRight(rt.left)
        self.ans.append(rt.val)
"""
class Solution:
    def boundaryOfBinaryTree(self, root):
        self.ans = []
        if(root == None):
            return self.ans
        self.ans.append(root.val)
        self.dfs(root.left, True, False)
        self.dfs(root.right, False, True)
        return self.ans

    def dfs(self, root, lft, rgt):
        if(root == None):
            return
        if(root.left == None and root.right == None):
            self.ans.append(root.val)
            return
        if(lft):
            self.ans.append(root.val)
        self.dfs(root.left, lft, rgt and root.right == None)
        self.dfs(root.right, lft and root.left == None, rgt)
"""    
        
        
        
        
        if(rgt):
            self.ans.append(root.val)