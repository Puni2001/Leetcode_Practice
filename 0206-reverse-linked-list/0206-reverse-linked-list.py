# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
         h
         1 -> 2 -> 3 -> 4 -> 5
  prev  curr next_node 

        ponites prev to None and curr to head 
        store the next_node 
        curr.next connect prev 
        move prev to curr
        curr to next node 
        
        """
        prev = None 
        curr = head 
        while curr:
          next_node = curr.next
          curr.next = prev
          prev = curr
          curr = next_node

        return prev 