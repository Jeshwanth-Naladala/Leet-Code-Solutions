# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.right = self.increasingBST(root.right)
        inorderPredecessor = self.helper(root.left)
        newRoot = self.increasingBST(root.left) if root.left else root
        if inorderPredecessor:
            inorderPredecessor.right = root
            root.left = None
        return newRoot
        
    def helper(self, root: TreeNode):
        if not root:
            return root
        while root.right:
            root = root.right
        return root