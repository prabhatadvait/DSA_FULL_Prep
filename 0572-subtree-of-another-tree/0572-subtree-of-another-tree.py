# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(p, q):
            if not p or not q:
                return p == q
            return (
                p.val == q.val and
                sameTree(p.left, q.left) and
                sameTree(p.right, q.right)
            )

        # ---------------------------
        # Missing subtree check logic
        # ---------------------------

        if not root:
            return False

        # If the current node matches subRoot
        if sameTree(root, subRoot):
            return True

        # Otherwise check left and right subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
