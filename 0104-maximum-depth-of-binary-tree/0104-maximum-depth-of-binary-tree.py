# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def fun(root):
            if root==None:
                return 0
            left_depth = fun(root.left)
            right_depth = fun(root.right)
            return max(left_depth,right_depth)+1
        return fun(root)