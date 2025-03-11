class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]

        # Detect cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Find entry point
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow