class Solution(object):
  def merge(self, arrayOfArrays):
    """
    input: int[][] arrayOfArrays
    return: int[]
    """
    import heapq
    heap = []
    for i in range(len(arrayOfArrays)):
      # the fist element to heap
      if len(arrayOfArrays[i]):
        heap.append((arrayOfArrays[i][0], i, 0))
    heapq.heapify(heap)
    ret = []
    while heap:
      val, index_a, index_i = heapq.heappop(heap)
      ret.append(val)
      if index_i + 1 < len(arrayOfArrays[index_a]):
        heapq.heappush(heap, (arrayOfArrays[index_a][index_i + 1], index_a, index_i + 1))
    return ret