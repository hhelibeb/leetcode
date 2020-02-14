# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.dfs(root) != -1

    def dfs(self, node: TreeNode) -> int:
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        if left == -1 or right == -1 or abs(left-right) > 1:
            return -1
        return max(left, right) + 1
