class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isMirror(left, right):
            # Both are empty
            if not left and not right:
                return True

            # One is empty
            if not left or not right:
                return False

            # Values must match and children must be mirrored
            return (left.val == right.val and
                    isMirror(left.left, right.right) and
                    isMirror(left.right, right.left))

        return isMirror(root.left, root.right)