class MyQueue:
    # Two stacks, one queue: in_stack takes pushes, out_stack serves pops.
    # Pouring one stack into another reverses it, so the oldest element ends up
    # on top of out_stack — exactly the queue front.
    # Invariant: out_stack holds the front of the queue in pop order, in_stack
    # holds the back in push order. Elements move in_stack -> out_stack only
    # when out_stack is empty, which is what keeps the amortized cost O(1).

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def _refill_out_stack(self) -> None:
        # Only when out_stack is empty. Pouring early would drop newer elements
        # on top of older ones and break FIFO order.
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._refill_out_stack()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._refill_out_stack()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
