# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
            dummy = ListNode(0, head)
            prev_group = dummy

            while True:
                # Check if there are at least k nodes left
                kth = prev_group
                for _ in range(k):
                    kth = kth.next
                    if not kth:
                        return dummy.next  # Less than k nodes left, return head
                
                # Reverse k nodes
                prev, curr = kth.next, prev_group.next
                for _ in range(k):
                    next_node = curr.next
                    curr.next = prev
                    prev, curr = curr, next_node

                # Connect reversed group with the rest
                temp = prev_group.next
                prev_group.next = prev
                prev_group = temp
