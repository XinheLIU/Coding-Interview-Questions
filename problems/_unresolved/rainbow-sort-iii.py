class Solution(object):
  def rainbowSortII(self, colors):
    """
    input: int[] array
    return: int[]
    """
    # bucket sort also works
    self.sort(colors, 0, 3, 0, len(colors) - 1)
    return colors
  
  def sort(self, colors, color_from, color_to, index_from, index_to):
    if color_from == color_to or index_from == index_to:
      return
    color = (color_from + color_to ) // 2
    l, r = index_from, index_to
    while l <= r:
      while l <= r and colors[l] <= color:
        l += 1
      while l <= r and colors[r] > color:
        r -= 1
      if l <= r:
        colors[l], colors[r] = colors[r], colors[l]
        l += 1
        r -= 1
    self.sort(colors, color_from, color, index_from, r)
    self.sort(colors, color + 1, color_to, l, index_to)
