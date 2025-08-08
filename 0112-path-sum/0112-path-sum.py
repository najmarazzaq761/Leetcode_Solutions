# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        # Check if it's a leaf node
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recursively check left and right subtrees
        left_has_path = self.hasPathSum(root.left, targetSum - root.val)
        right_has_path = self.hasPathSum(root.right, targetSum - root.val)
        
        return left_has_path or right_has_path