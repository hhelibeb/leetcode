from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    temp = []
    if not root:
        return
    queue = deque()
    queue.append(root)
    while True:
        if not queue:
            break
        length = len(queue)
        for i in range(length):
            node = queue.popleft()
            temp += [node.val]
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(list(temp))
        temp = []
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()
