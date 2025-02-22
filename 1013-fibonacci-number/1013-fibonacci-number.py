class Solution:
    def fib(self, n: int) -> int:
        """
        0 -> 1  1 -> 1 
        n - 1 
        """
        if n == 0: 
            return 0
        if n == 1:
            return 1
        
        return self.fib(n-1)+ self.fib(n-2)