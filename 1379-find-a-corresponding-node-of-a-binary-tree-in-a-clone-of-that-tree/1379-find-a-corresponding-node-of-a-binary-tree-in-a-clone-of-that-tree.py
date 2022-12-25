# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original == target:
            return cloned
        elif original == None:
            return None
        else:
            temp = self.getTargetCopy(original.left, cloned.left, target) 
            return temp if temp != None else self.getTargetCopy(original.right, cloned.right, target)