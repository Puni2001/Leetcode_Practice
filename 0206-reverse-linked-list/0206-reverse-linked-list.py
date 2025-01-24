# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        head
         |
         v
None    1 -> 2 -> 3 -> 4 -> 5 -> None 
  |      |    |
prev    curr next_node

        """
        prev = None
        curr = head 
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
        

