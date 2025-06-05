# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()

        l3 = head
        carry = 0

        while l1 and l2:
            l3.next = ListNode()
            l3 = l3.next
            l3.val = l1.val + l2.val

            if carry:
                l3.val += 1
                carry = 0

            if l3.val >= 10:
                carry = 1
                l3.val -= 10

            l1 = l1.next
            l2 = l2.next
            

        while l1:
            l3.next = ListNode()
            l3 = l3.next
            l3.val = l1.val

            if carry:
                l3.val += 1
                carry = 0

            if l3.val >= 10:
                carry = 1
                l3.val -= 10
            
            l1 = l1.next

        while l2:
            l3.next = ListNode()
            l3 = l3.next
            l3.val = l2.val

            if carry:
                l3.val += 1
                carry = 0

            if l3.val >= 10:
                carry = 1
                l3.val -= 10
            
            l2 = l2.next

        if carry == 1:
            l3.next = ListNode()
            l3 = l3.next
            l3.val = 1

        return head.next