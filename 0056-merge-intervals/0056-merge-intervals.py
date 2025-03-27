class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
      if not intervals:
          return []
      
      # Step 1: Sort the intervals based on start time
      intervals.sort()  # O(N log N)

      merged = [intervals[0]]  # Initialize with first interval

      for i in range(1, len(intervals)):
          prev = merged[-1]  # Last interval in the merged list
        
          curr = intervals[i]  # Current interval
  
          if prev[1] >= curr[0]:  # Overlapping case
              merged[-1] = [prev[0], max(prev[1], curr[1])]  # Merge
          else:
              merged.append(curr)  # No overlap, add new interval

      return merged
