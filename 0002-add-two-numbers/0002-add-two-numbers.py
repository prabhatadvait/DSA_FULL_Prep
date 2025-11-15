# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        final = None
        temp = None
        carry = 0

        while(l1 or l2):
            sum=carry

            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next
            node = ListNode(sum%10)

            if temp is None:
                temp =final= node
            else:
                temp.next = node
                temp = temp.next

            carry = sum//10
        if carry>0:
            node = ListNode(carry)
            temp.next = node
        return final
