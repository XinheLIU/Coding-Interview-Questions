class Solution(object):
  def rightShift(self, input, k):
    """
    input: string input, int n
    return: string
    """
    if not input or not len(input):
      return input
    n = len(input)
    k %= n
    array = list(input)
    return ''.join(array[n-k:n] + array[:n-k])