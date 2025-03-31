from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # If we have only one bag, no cuts are needed, so the difference is 0
        if k == 1:
            return 0

        # Add the weights of every two adjacent marbles
        arr = [weights[i] + weights[i + 1] for i in range(len(weights) - 1)]

        # Sort the list of sums in ascending order
        arr.sort()
        
        # Find the sum of the smallest (k - 1) sums (cheapest cuts)
        mn = sum(arr[:k - 1])

        # Find the sum of the largest (k - 1) sums (most expensive cuts)
        mx = sum(arr[-(k - 1):])

        # Return the difference between the most expensive and the cheapest cuts
        return mx - mn