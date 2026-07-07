class Solution:
    """
    @param root, the root of tree
    @return: a doubly list node
    """
    def bstToDoublyList(self, root):
        if not root:
        	return root
        pre, head =  DoublyListNode(None), DoublyListNode(None)
        self.inorder(root.left, pre, head)
        pre.right = head
        head.left = pre
        return head

        head = None
        prev = None
        for val in dfs:
            node = DoublyListNode(val)
            if head is None:
                head = node
            else:
                prev.next = node
            node.prev = prev
            prev = node
        return head

    def inorder(self, node, pre, head):
    	if not node:
    		return None
    	# in order
    	self.inorder(node.left, pre, head)
    	if not head:
    		head, pre = node, node
    	else:
    		pre.right = node
    		node.left = pre
    		pre = node
    	self.inorder(node.right, pre, head)
        
""" 
    def bstToDoublyList(self, root):
        # Write your code here
        dfs = []
        self.getDfs(root, dfs)
        if len(dfs) == 0:
            return None

        head = None
        prev = None
        for val in dfs:
            node = DoublyListNode(val)
            if head is None:
                head = node
            else:
                prev.next = node
            node.prev = prev
            prev = node
        return head

    def getDfs(self, root, dfs):
        if root is None:
            return
        self.getDfs(root.left, dfs)
        dfs.append(root.val)
        self.getDfs(root.right, dfs)
"""  
        
        
