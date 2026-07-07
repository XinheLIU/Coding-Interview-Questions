from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        self.queue = deque([])
        self.size = size
        self.sum = 0.0
        

    def next(self, val):
        if len(self.queue) == self.size:
            self.sum -= self.queue.popleft()
            
        self.sum += val
        self.queue.append(val)
        return self.sum / len(self.queue)