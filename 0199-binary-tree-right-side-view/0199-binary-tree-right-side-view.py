# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        
        q = deque()
        q.append(root)
        
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                
                # Last node of each level
                if i == size - 1:
                    ans.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return ans