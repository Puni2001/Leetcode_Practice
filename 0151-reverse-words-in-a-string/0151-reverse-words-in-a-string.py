class Solution:
    def reverseWords(self, s: str) -> str:
      s = s.strip()  # Remove leading/trailing spaces
      words = []
      left = 0

      # Split words manually
      while left < len(s):
          while left < len(s) and s[left] == " ":  # Skip spaces
              left += 1
          if left >= len(s):
              break
          right = left
          while right < len(s) and s[right] != " ":  # Find end of word
              right += 1
          words.append(s[left:right])
          left = right  # Move to next word

      return " ".join(reversed(words))  # Reverse words and join
          
          

