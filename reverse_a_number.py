class Solution:
    def reverse(self, x: int) -> int:
      # Define the maximum and minimum 32-bit signed integer values
      MAX_INT = 2**31 - 1
      MIN_INT = -2**31
      
      # Initialize result variable
      result = 0
      
      # Handle negative numbers by marking a flag
      negative = x < 0
      
      # Take the absolute value of x
      x = abs(x)
      
      while x != 0:
          # Extract the last digit of x
          digit = x % 10
          
          # Update the result by shifting digits to the left and adding the new digit
          result = result * 10 + digit
          
          # Check if the result exceeds the 32-bit integer range
          if result > MAX_INT or result < MIN_INT:
              return 0
          
          # Remove the last digit from x
          x //= 10
      
      # If the original number was negative, make the result negative
      if negative:
          result = -result
      
      return result
