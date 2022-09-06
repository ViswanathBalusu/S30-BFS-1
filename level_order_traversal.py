from typing import Optional, List
from queue import Queue


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        q = Queue()
        q.put(root)
        while not q.empty():
            _size = q.qsize()
            temp_list = []
            for i in range(_size):
                curr = q.get()
                temp_list.append(curr.val)
                if curr.left is not None:
                    q.put(curr.left)
                if curr.right is not None:
                    q.put(curr.right)
            result.append(temp_list)
        return result


# Using DFS
class Solution2:
    def __init__(self):
        self.result = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        self.level_order_helper(root, 0)
        return self.result

    def level_order_helper(self, root: Optional[TreeNode], depth: int):
        if root is None:
            return
        if len(self.result) - 1 < depth:
            self.result.insert(depth, [])
        self.result[depth].append(root.val)
        self.level_order_helper(root.left, depth+1)
        self.level_order_helper(root.right, depth+1)

