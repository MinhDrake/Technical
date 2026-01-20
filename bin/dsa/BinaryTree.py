from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def in_order(node):
        if not node:
            return []
        return in_order(node.left) + [node.val] + in_order(node.right)

    def level_order(node):
        if not node:
            return []
        result, queue = [], deque([node])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)
            result.append(level)
        return result
