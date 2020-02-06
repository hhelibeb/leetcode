from typing import List
from collections import deque


# Definition for a binary tree node.     
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []
        queue = deque([root])
        while queue:
            length = len(queue)
            temp = 0
            for i in range(length):
                node = queue.popleft()
                temp += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result += [temp/length]
        return result
