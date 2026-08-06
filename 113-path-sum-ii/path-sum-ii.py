# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pathSum(
        self, root: Optional[TreeNode], targetSum: int
    ) -> List[List[int]]:
        result = []

        def dfs(node, path, remaining_sum):
            if not node:
                return

            path.append(node.val)

            # Check if it's a leaf node with the target path sum
            if not node.left and not node.right and node.val == remaining_sum:
                result.append(list(path))

            dfs(node.left, path, remaining_sum - node.val)
            dfs(node.right, path, remaining_sum - node.val)

            # Backtrack
            path.pop()

        dfs(root, [], targetSum)
        return result