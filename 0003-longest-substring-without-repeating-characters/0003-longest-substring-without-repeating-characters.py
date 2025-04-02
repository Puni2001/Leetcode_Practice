class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # using sliding window 
        """
             "abcabcbb"
                  l 
                    r 

            1. char_set = set()  to avoid duplicates 
            2. longest = 0 to tract max so far 
            3. use two pointer left and right 
            4. window = right - left + 1
        
        """

        longest = 0 
        n  = len(s)
        char_set = set()
        left = 0

        for right in range(n):
          while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
          char_set.add(s[right])
          window = right - left + 1

          longest = max(longest, window)

        return longest 
            