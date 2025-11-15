# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        dummy = ListNode(0)
        dummy.next = head

        fast = slow = dummy
        while(n>=0):
            fast = fast.next
            n-=1
        
        while (fast):
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next