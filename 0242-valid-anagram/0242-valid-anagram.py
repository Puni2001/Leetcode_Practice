class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        check the len of s == t if not return false 
        count = [0] * 26 
        1+ if char in s 
        1- if char in t 

        finally we check all count is 0 or not is not then it is not anagram 
        
        """
        if len(s) != len(t):
            return False 

        
        count = [0] * 26

        for char_s , char_t in zip(s,t):
            count[ord(char_s)-ord('a')] += 1
            count[ord(char_t)-ord('a')] -= 1

        return all(x==0 for x in count)