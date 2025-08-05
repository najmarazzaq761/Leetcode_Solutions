# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        def dfs(node,path):
            if not node:
                return 
            if not node.left and not node.right:
                result.append(path+str(node.val))
                return 
            if node.left:
                dfs(node.left, path+str(node.val)+"->")
            if node.right:
                dfs(node.right, path+str(node.val)+"->")
        dfs(root,"")
        return result