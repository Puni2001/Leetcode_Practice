class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False  
            
        if s == "": return True 

        j = 0 

        for i in range(len(t)):
            if s[j] == t[i]:
                if j == len(s)-1:
                    return True
                j += 1
        return False

            
