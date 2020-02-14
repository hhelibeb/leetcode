# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum1(self, root, sum):
        if not root:
            return False
        if root and not root.left and not root.right and root.val == sum:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


s = Solution()
right = TreeNode(2)
left = TreeNode(0)
root = TreeNode(1)
root.right = right
root.left = left
print(s.hasPathSum(root, 1))
