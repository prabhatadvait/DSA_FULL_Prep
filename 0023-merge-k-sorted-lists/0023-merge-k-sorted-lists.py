# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        # Push the head node of each non-empty list into the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        # Create a dummy node to build the result list
        dummy = ListNode(0)
        tail = dummy

        # While the heap is not empty
        while min_heap:
            # Extract the node with the smallest value
            val, i, node = heapq.heappop(min_heap)

            # Add it to the result list
            tail.next = node
            tail = tail.next

            # If there's a next node, push it into the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        # Return the head of the merged list
        return dummy.next