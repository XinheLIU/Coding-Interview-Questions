'''
Given a string, remove all leading/trailing/duplicated empty spaces.

Assumptions:

The given string is not null.
Examples:

“  a” --> “a”
“   I     love MTV ” --> “I love MTV”

'''
class Solution(object):
  def removeSpaces(self, s):
    """
    input: string input
    return: string
    """
    array, end = list(s), 0
    for i in range(len(array)):
      if array[i] == ' ' and (i == 0 or array[i-1] == ' '):
        continue
      array[end] = array[i]
      end += 1
    # trailing space
    while end > 0 and array[end - 1] == ' ':
      end -= 1
    return ''.join(array[:end])