# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        
        output = []
        self.inorder(root, output)
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False
        return True
    
    # Fun fact: Inorder traversal leads to a sorted array if it is a Valid Binary Search Tree.
    def inorder(self, root, output): 
            if root is None:
                return 
            self.inorder(root.left, output)
            output.append(root.val)
            self.inorder(root.right, output)
        