"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Clone nodes and interweave them with original list
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next

        # Step 2: Copy random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate cloned list from original
        curr, new_head = head, head.next
        clone = new_head
        while curr:
            curr.next = curr.next.next
            clone.next = clone.next.next if clone.next else None
            curr = curr.next
            clone = clone.next

        return new_head
