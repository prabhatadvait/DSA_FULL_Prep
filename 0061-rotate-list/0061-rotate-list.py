# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0:
            return head
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        k = k%len(arr)
        ans = arr[-k:]+arr[:-k]
        new_head = ListNode(ans[0])
        curr = new_head
        for i in range(1,len(ans)):
            curr.next = ListNode(ans[i])
            curr = curr.next
        return new_head