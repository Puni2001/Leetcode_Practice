class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Brute -> checking with nested  loops all substrings and updating the longest 
        Time -> O(N^2)

        Optimize -> Sliding window 

            s = "abcabcbb"   longest = 3  char_set = set()
                  l
                     r
            check window is valid update longest and char_set and move right pointer
            else remove char_set of s[left] move right pointer 
        """
        char_set = set()
        longest = 0
        left = 0
       
        for right in range(len(s)):
            
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            longest = max(longest, right - left + 1 )

        return longest 