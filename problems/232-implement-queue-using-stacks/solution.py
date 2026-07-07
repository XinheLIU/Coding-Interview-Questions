class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def adjust(self):
        if not len(self.stack2):
            while len(self.stack1):
                self.stack2.append(self.stack1.pop())
                
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # input stack
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # output stack
        self.adjust()
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.adjust()
        if len(self.stack2):
            return self.stack2[-1]     

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not len(self.stack1) and not len(self.stack2)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()