class Solution:
    def minWindow(self, s: str, t: str) -> str:
       
      if not s or not t:
          return ""

      t_count = Counter(t)
      window_count = {}
      l, r = 0, 0
      required = len(t_count)  # Number of unique chars in t that must be in window
      formed = 0  # When window contains all characters with the required frequency

      min_len = float("inf")
      min_window = ""

      while r < len(s):
          char = s[r]
          window_count[char] = window_count.get(char, 0) + 1

          if char in t_count and window_count[char] == t_count[char]:
              formed += 1  # We found a required character in correct count

          while formed == required:  # Try to shrink from left
              if (r - l + 1) < min_len:
                  min_len = r - l + 1
                  min_window = s[l:r+1]

              # Remove from window and move left pointer
              window_count[s[l]] -= 1
              if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                  formed -= 1  # We lost a required character

              l += 1

          r += 1  # Expand the right pointer

      return min_window