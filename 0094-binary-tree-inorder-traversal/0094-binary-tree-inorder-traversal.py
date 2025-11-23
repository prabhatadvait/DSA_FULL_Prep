# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        p = []
        def fun(root,p):
            if not root:
                return
            fun(root.left,p)
            p.append(root.val)
            fun(root.right,p)
        fun(root,p)
        return p