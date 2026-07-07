class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # semantics for self._head: it will always refer to the head node of the internal singly linked list
        self._head = None
        # cahces the number of nodes 
        self._size = 0
        self._tail = None

    def _get(self, index):
        # assuming index is in range[0, size)
        node = self._head
        for _ in xrange(index):
            node = node.next
        return node
    
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self._size:
            return -1
        return self._get(index).val      

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        if self._size  == 0:
            self._head = self._tail = ListNode(val)
        else:
            new_head = ListNode(val)
            new_head.next = self._head
            self._head = new_head
        self._size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if self._size  == 0:
            self._head = self._tail = ListNode(val)
        else:
            self._tail.next = ListNode(val)
            self._tail = self._tail.next
        self._size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self._size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self._size:
            self.addAtTail(val)
        else:
            # pre-node
            node = self._get(index - 1)
            new_node = ListNode(val)
            new_node.next = node.next
            node.next = new_node
            self._size += 1   

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self._size:
            return
        if index == 0:
            new_head = self._head.next
            self._head.next = None
            self._head = new_head
            # empty list
            if not self._head:
                self._tail = None
        else:
            # pre-node
            node = self._get(index - 1)
            remove_node = node.next
            node.next = remove_node.next
            remove_node.next = None
            # removed the original tail
            if index == self._size - 1:
                self._tail = node
        self._size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)