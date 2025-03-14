class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def canFinish(k):
            return sum(math.ceil(p / k) for p in piles) <= h

        while left < right:
            mid = (left + right) // 2
            if canFinish(mid):
                right = mid  # Try smaller k
            else:
                left = mid + 1  # Increase k

        return left
