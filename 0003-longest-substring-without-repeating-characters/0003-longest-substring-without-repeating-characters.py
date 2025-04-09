class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0 
        longest = 0

        for right in range(len(s)):
          while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

          char_set.add(s[right])
          current_window = right - left + 1 
          longest = max(longest, current_window)
         
        return longest 
