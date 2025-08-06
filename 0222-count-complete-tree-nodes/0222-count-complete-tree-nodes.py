# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def getHeightLeft(node):
            height = 0
            while node:
                node = node.left
                height += 1
            return height

        def getHeightRight(node):
            height = 0
            while node:
                node = node.right
                height += 1
            return height

        left = getHeightLeft(root)
        right = getHeightRight(root)

        if left == right:
            return (1 << left) - 1  # 2^left - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
