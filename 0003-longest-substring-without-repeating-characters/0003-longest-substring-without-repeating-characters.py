class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        longest = 0
        n = len(s)
        left = 0 

        for right in range(n):
          while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

          char_set.add(s[right])
          longest = max(longest, right-left+1)
        
        return longest 
