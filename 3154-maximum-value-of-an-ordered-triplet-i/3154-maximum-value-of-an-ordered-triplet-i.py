class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        highest, diff, ans = 0, 0, 0
        for k in nums:
            ans = max(ans, diff*k)
            diff = max(highest - k, diff)
            highest = max(highest, k)
        return ans