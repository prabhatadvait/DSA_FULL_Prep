# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        linkedlist = []
        temp = head
        while temp:
            linkedlist.append(temp.val)
            temp = temp.next
        return linkedlist[:]==linkedlist[::-1]