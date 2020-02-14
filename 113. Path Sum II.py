from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result = []
        temp = []
        self.dfs(root, sum, temp, result)
        return result

    def dfs(self, node: TreeNode, sum: int, temp: List[int], result: List[List[int]]):
        if not node:
            return
        temp += [node.val]
        if not node.left and not node.right and sum == node.val:
            result.append(list(temp))
        else:
            self.dfs(node.left, sum - node.val, temp, result)
            self.dfs(node.right, sum - node.val, temp, result)
        temp.pop()