import collections
class LRUCache:

    def __init__(self, capacity: 'int'):
        #  standard way is to use double linked list - the head is the lru element 
        self.dict = collections.OrderedDict()
        self.remain = capacity
        
    def get(self, key: 'int') -> 'int':
        if key not in self.dict:
            return -1
        # pop/delete then insert to head position
        v = self.dict.pop(key)
        self.dict[key] = v
        return v

    def put(self, key: 'int', value: 'int') -> 'None':
        if key in self.dict:
            self.dict.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dict.popitem(last=False)
        self.dict[key] = value
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''

class LinkedNode:   
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.key_to_prev = {}
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.capacity = capacity
    
    def push_back(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node
    
    def pop_front(self):
        # 删除头部
        head = self.dummy.next
        del self.key_to_prev[head.key]
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy
        
    # change "prev->node->next...->tail"
    # to "prev->next->...->tail->node"
    def kick(self, prev):    #将数据移动至尾部
        node = prev.next
        if node == self.tail:
            return
        prev.next = node.next
        if node.next is not None:
            self.key_to_prev[node.next.key] = prev
            node.next = None
        self.push_back(node)

    # @return an integer
    def get(self, key):		#获取数据
        if key not in self.key_to_prev:
            return -1
        self.kick(self.key_to_prev[key])
        return self.key_to_prev[key].next.value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def put(self, key, value):     #数据放入缓存
        if key in self.key_to_prev:	   
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.value = value
        else:
            self.push_back(LinkedNode(key, value))  #如果key不存在，则存入新节点
            if len(self.key_to_prev) > self.capacity:		#如果缓存超出上限
                self.pop_front()
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
'''