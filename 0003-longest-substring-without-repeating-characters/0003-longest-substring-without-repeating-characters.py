class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window 
        longest = 0
        left = 0
        seen = set()

        n = len(s)

        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])

                left += 1

            seen.add(s[right])
            w = ( right - left ) + 1
            longest = max(w,longest)
        
        return longest