# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head 
        while curr:
          while stack and stack[-1].val < curr.val:
            stack.pop()
          stack.append(curr)
          curr=curr.next 
        
        dummy = ListNode(0)
        prev = dummy 

        for node in stack:
          prev.next = node 
          prev = prev.next 

        prev.next = None 

        return dummy.next 