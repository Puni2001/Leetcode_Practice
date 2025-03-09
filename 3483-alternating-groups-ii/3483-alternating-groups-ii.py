class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
      if not colors:
        return 0
      n = len(colors)
      l = 0 
      groups = 0
      
      for r in range(1,n+k-1):

        if colors[r % n ]==colors[(r-1) % n]: 
          l = r
        if r - l + 1 > k:
          l += 1
        if r - l + 1 == k:
          groups += 1

      return groups

