class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        res = []
        dq = deque()  # Store indices of useful elements

        for i in range(len(nums)):
            # Remove elements out of the window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove elements smaller than current element
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add current element index
            dq.append(i)

            # Append max to result (only after first k elements)
            if i >= k - 1:
                res.append(nums[dq[0]])  # Max is always at dq[0]

        return res