# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        p = []
        def fun(root,p):
            if not root:
                return 
            fun(root.left,p)
            fun(root.right,p)
            p.append(root.val)
        fun(root,p)
        return p