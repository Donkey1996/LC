import sys
from collections import deque
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree

"""
102. Binary Tree Level Order Traversal
Medium

Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).
"""


class Solution:
    """
    BFS
    """

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            n = len(q)
            current_level = []
            for i in range(n):
                current = q.popleft()
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
                current_level += [current.val]
            res += [current_level]
        return res


def main():
    tests = [
        {"vals": [3, 9, 20, None, None, 15, 7], "traversal": [[3], [9, 20], [15, 7]]},
        {"vals": [1], "traversal": [[1]]},
    ]

    i = 0
    for test in tests:
        i += 1
        vals = test["vals"]
        root = list_to_tree(vals)
        solver = Solution()
        print(solver.levelOrder(root))
        assert solver.levelOrder(root) == test["traversal"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
