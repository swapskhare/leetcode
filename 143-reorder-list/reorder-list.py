# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None

        curr = head2
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        dummy = ListNode()
        temp = dummy
        fast = prev
        while fast and head:
            temp.next = head
            head = head.next
            temp = temp.next
            temp.next = fast
            fast = fast.next
            temp = temp.next

        temp.next = head or fast

        return dummy.next
            

            


        
        