from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth = 0
        if not root:
            return depth
        queue = deque([root])
        while queue:
            depth += 1
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)
        return depth
