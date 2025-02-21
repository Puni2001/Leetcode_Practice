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
prev   curr
        prev = None 
        head = curr 
        
        traverse the linked list untill head is None 
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node 

        return prev 

        """

        prev = None 
        curr = head

        while curr: # until we traverse entire linked list 
            next_node = curr.next
            curr.next = prev 
            prev = curr 
            curr = next_node 

        return prev
