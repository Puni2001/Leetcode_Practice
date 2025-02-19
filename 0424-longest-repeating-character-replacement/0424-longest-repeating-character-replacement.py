class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        optimal -> using sliding window 
        s = 'AABABABAAAAB'
             l
                 r                  longest =  0  count_char = {A: 0 , B : 0}
        while w - max(char_count[s[r]]) > k:

        """
        longest = 0
        counts = [0] * 26
        left = 0

        for right in range(len(s)):
            counts[ord(s[right]) - ord('A')] += 1
            while (right-left)+1 - max(counts) > k:
                counts[ord(s[left]) - ord('A')] -= 1
                left += 1

            longest = max(longest, (right-left)+1)

        return longest
           

