# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        p = []
        def fun(root,p):
            if not root:
                return 
            p.append(root.val)
            fun(root.left,p)
            fun(root.right,p)
        fun(root,p)    
        return p
