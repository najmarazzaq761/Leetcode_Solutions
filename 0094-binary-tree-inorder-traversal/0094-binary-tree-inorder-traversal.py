# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # result = []
        # stack = []
        # current = root
        # while current or stack:
        #     while current:
        #         stack.append(current)
        #         current = current.left
        #     current = stack.pop()
        #     result.append(current.val)

        #     current = current.right
        # return result

                        # recursion
        def inorder(node, list1):
            
            if not node:
                return None
            inorder(node.left, list1)
            list1.append(node.val)
            inorder(node.right, list1)
        list1 = []
        inorder(root, list1)
        return list1
