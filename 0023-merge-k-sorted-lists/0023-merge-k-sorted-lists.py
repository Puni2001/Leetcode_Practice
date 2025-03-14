# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
    
        # Initialize the heap with the head nodes of all lists
        for i, l in enumerate(lists):
            if l:
                heappush(min_heap, (l.val, i, l))  # (value, index, node)

        dummy = ListNode(0)
        curr = dummy

        while min_heap:
            val, i, node = heappop(min_heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next