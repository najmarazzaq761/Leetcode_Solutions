# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def recursive(left, right):
            if right < left:
                return [None]
            if left == right:
                return [TreeNode(left)]
            output = []
            for root in range(left, right+1):
                left_side = recursive(left, root-1)
                right_side = recursive(root+1, right)

                for l in left_side:
                    for r in right_side:
                        subtree = TreeNode(root, l, r)
                        output.append(subtree)
            return output
        return recursive(1,n)