class Solution:
  def addBinary(self, a: str, b: str) -> str:
    """
    input: string a, string b
    return: string
    """
    if not a or not len(a): return b
    if not b or not len(b): return a
    i, j = len(a) - 1, len(b) - 1
    ret, carry = "", 0
    while i >= 0 or j >= 0:
      if i >= 0: 
        carry += int(a[i])
        i -= 1
      if j >= 0: 
        carry += int(b[j])
        j -= 1
      digit = carry % 2
      carry //= 2
      ret = str(digit) + ret
    if carry > 0: 
      ret = "1" + ret
    return ret