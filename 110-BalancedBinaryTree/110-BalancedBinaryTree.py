# Last updated: 8/21/2025, 1:11:18 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#for each node, find height of left and right subtree
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True
        
        def dfs(curr):
            leftHeight = 0
            rightHeight = 0
            leftBalanced = True
            rightBalanced = True    
            if curr.left is not None:
                leftHeight, leftBalanced = dfs(curr.left)
            if curr.right is not None:
                rightHeight, rightBalanced = dfs(curr.right)
            
            retBalanced = leftBalanced and rightBalanced and (abs(leftHeight-rightHeight)<=1)
            return 1 + max(leftHeight, rightHeight), retBalanced
        
        _, balanced = dfs(root)

        return balanced