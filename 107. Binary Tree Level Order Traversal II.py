from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = deque()
        if not root:
            return
        queue = deque([root])
        while queue:
            temp = []
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                temp += [node.val]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.appendleft(temp)
        return list(result)

