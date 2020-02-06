from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        seq = False
        result = []
        if not root:
            return
        queue = deque([root])
        while True:
            if not queue:
                break
            length = len(queue)
            temp = []
            for i in range(length):
                node = queue.popleft()
                temp += [node.val]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if seq:
                temp.reverse()
                seq = False
            else:
                seq = True
            result.append(list(temp))
        return result
