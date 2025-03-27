class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
      if not intervals:
        return []

      # Step 1: Sort intervals by start time
      intervals.sort()

      merged = [intervals[0]]  # Start with first interval

      for start, end in intervals[1:]:
          last_end = merged[-1][1]  # End of the last added interval

          if start <= last_end:  # Overlapping condition
              merged[-1][1] = max(last_end, end)  # Merge intervals
          else:
              merged.append([start, end])  # Add non-overlapping interval

      return merged
