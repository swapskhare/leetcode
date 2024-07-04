# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        left = head.next
        sum = 0

        while left.val!=0:
            sum+=left.val
            left = left.next

        head.next.val = sum

        head.next.next = self.mergeNodes(left)

        return head.next

