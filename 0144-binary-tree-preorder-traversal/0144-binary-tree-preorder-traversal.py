# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if not root:
        #   return []
        # result = []
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     result.append(node.val)
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        # return result

        def inorder(node, list1):
            
            if not node:
                return None
            
            list1.append(node.val)
            inorder(node.left, list1)
            inorder(node.right, list1)
        list1 = []
        inorder(root, list1)
        return list1