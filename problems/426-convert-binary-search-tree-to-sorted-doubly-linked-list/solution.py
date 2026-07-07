# different from Java, Cpp because of assignment issue, better use stack
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        head, tail = self.traverse(root)
        return head
        
    def traverse(self, root):
        # construct double linked list, return head, tail        
        head, tail = root, root
        
        if root.left:
            left_head, left_tail = self.traverse(root.left)
            left_tail.right = root
            root.left = left_tail
            head = left_head
        
        if root.right:
            right_head, right_tail = self.traverse(root.right)
            right_head.left = root
            root.right = right_head
            tail = right_tail
            
        head.left = tail
        tail.right = head
        return head, tail
        
"""
  def inorder(self, node):
        if not node: return
        left = node.left
        for n in self.inorder(left):
            yield n
        yield node
        right = node.right
        for n in self.inorder(right):
            yield n
    
    def treeToDoublyList(self, root):
        # Write your code here.
        if not root: return root
        head = None
        last = None
        prev = None
    	# iterate the tree like a list
        for v in self.inorder(root):
            if head is None: head = v
            last = v
            if prev is not None:
                prev.right = v
                v.left = prev
            prev = v
        head.left = last
        last.right = head
        return head
"""