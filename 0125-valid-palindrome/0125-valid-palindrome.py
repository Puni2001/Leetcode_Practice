class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = ''.join(c.lower() for c in s if c.isalnum())
        print(filtered_s)
        rev_s = filtered_s[::-1]
        print(rev_s)
        return filtered_s == rev_s