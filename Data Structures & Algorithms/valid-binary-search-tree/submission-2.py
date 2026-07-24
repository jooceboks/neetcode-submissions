# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
     def valid(node, mins, maxs):
            if not node:
                return True
            if not (mins < node.val < maxs):
                return False

            return valid(node.left, mins, node.val) and valid(node.right, node.val, maxs)
            
     return valid(root, float("-inf"), float("inf"))