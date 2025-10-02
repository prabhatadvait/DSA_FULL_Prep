# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(min_heap,(node.val,i,node))
        
        dummy = ListNode(0)
        tail = dummy

        while min_heap:
            val,i,node = heapq.heappop(min_heap)
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(min_heap,(node.next.val,i,node.next))
        return dummy.next