class Solution:
    def addTwoNumbers(self, list1, list2):
        l1 = list1
        l2 = list2
        cry = 0
        result = ListNode(0)
        temp = result
        
        while l1 is not None or l2 is not None:
            if l1 is not None:
                cry += l1.val
                l1 = l1.next
            if l2 is not None:
                cry += l2.val
                l2 = l2.next
            temp.next = ListNode(cry % 10)
            temp = temp.next
            cry = cry // 10
        
        if cry == 1:
            temp.next = ListNode(cry)
        
        return result.next