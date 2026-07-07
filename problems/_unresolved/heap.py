class BinHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def __minChild(self,i):
		if i * 2 + 1 > self.currentSize:
			return i * 2
		else:
			if self.heapList[i*2] < self.heapList[i*2+1]:
				return i * 2
			else:
				return i * 2 + 1

	def shiftDown(self,i):
		while (i * 2) <= self.currentSize:
			mc = self.__minChild(i)
			if self.heapList[i] > self.heapList[mc]:
				self.heapList[mc], self.heapList[i] = self.heapList[i], self.heapList[mc]
			i = mc

	def shiftUp(self,i):
		while i // 2 > 0:
			if self.heapList[i] < self.heapList[i // 2]:
				self.heapList[i // 2], self.heapList[i]  = self.heapList[i], self.heapList[i // 2]
			i = i // 2

	def insert(self,k):
		self.heapList.append(k)
		self.currentSize = self.currentSize + 1
		self.shiftUp(self.currentSize)

	def delMin(self):
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.heapList.pop()
		self.shiftDown(1)
		return retval

	def buildHeap(self,alist):
		i = len(alist) // 2
		self.currentSize = len(alist)
		self.heapList = [0] + alist[:]
		while (i > 0):
			self.shiftDown(i)
			i = i - 1