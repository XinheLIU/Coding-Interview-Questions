class Solution(object):
  def merge(self, arr, L, R):
    i = j = k = 0
    while i < len(L) and j < len(R): 
      if L[i] < R[j]: 
        arr[k] = L[i] 
        i+=1
      else: 
        arr[k] = R[j] 
        j+=1
      k+=1
     # Checking if any element was left 
    while i < len(L): 
      arr[k] = L[i] 
      i+=1
      k+=1
    while j < len(R): 
      arr[k] = R[j] 
      j+=1
      k+=1
       
  def mergeSort(self, arr):
    """
    input: int[] array
    return: int[]
    """
    if len(arr) > 1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
        self.mergeSort(L) # Sorting the first half 
        self.mergeSort(R) # Sorting the second half 
        self.merge(arr, L, R)
    return arr
'''
# no side effects version
class Solution(object):
  def merge(self, L, R):
    ret = []
    i = j = 0
    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        ret.append(L[i])
        i += 1
      else:
        ret.append(R[j])
        j += 1
    if i < len(L):
      ret.extend(L[i:])
    if j < len(R):
      ret.extend(R[j:])
    return ret
        
       
  def mergeSort(self, arr):
    """
    input: int[] array
    return: int[]
    """
    if len(arr) > 1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = self.mergeSort(arr[:mid]) # Sorting the first half 
        R = self.mergeSort(arr[mid:]) # Sorting the second half 
        return self.merge(L, R)
    return arr
'''