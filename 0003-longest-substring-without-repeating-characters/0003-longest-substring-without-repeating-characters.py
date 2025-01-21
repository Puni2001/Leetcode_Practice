class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        seen = set()
        longest = 0 
        l = 0 
       

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            w = (r - l) + 1 
            longest = max(longest, w)
            seen.add(s[r])

        return longest

            