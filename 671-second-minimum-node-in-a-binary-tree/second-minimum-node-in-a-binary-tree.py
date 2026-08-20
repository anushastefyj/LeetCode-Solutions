# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        
        min_val = root.val
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            
            # Found a candidate strictly greater than root.val
            if node.val > min_val:
                return node.val
            
            # If node.val == min_val, check both subtrees
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If both subtrees have candidates, pick the smaller one
            if left != -1 and right != -1:
                return min(left, right)
            
            # Otherwise return whichever subtree found a candidate (or -1)
            return max(left, right)

        return dfs(root)