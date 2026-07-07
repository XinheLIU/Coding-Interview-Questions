class Solution(object):
  def remove(self, input, t):
    """
    input: string input, string t
    return: string
    """
    charToRemove = set(t)
    ret = []
    for letter in input:
      if letter not in t:
        ret.append(letter)
    return "".join(ret)