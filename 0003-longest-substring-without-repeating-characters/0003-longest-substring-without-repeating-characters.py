class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        longest = 0

        # Expand the window as we go 
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            window_length = ( right - left) + 1
            longest = max(longest, window_length)

        return longest