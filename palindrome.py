# 9. Palindrome Number
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # store a reverse number in rev variable 
        rev = 0
        # store a actual number to reverse in duplicate name dup
        dup = x
        # iterate till x greater than zero 
        while x > 0:
          # to get a last digit use modolus operator 
          ld = x % 10
          # once get last digit update rev like 121 % 10 = 1
          # rev = 0 * 10 --> 0 + 1 = 1 
          rev = ( rev * 10) + ld
        # remove last digit from the x by // --> 121 // 10  --> 12 because ignore decimal points 
          x = x // 10

        # out of the loop compare the rev and dup
        if dup == rev:
          return True
        else:
          return False
