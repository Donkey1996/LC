import sys
from collections import deque, defaultdict
from typing import Optional

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree

"""
104. Maximum Depth of Binary Tree
Easy

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.
"""


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        visited = defaultdict(list)
        q = deque([(root, 1)])
        while q:
            node, depth = q.popleft()
            visited[depth].extend([node])
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))

        return sorted(visited)[-1]


def main():
    tests = [
        {"vals": [3, 9, 20, None, None, 15, 7], "result": 3,},
        {"vals": [1, None, 2], "result": 2},
        {"vals": [], "result": 0},
    ]

    i = 0
    for test in tests:
        i += 1
        vals = test["vals"]
        root = list_to_tree(vals)
        solver = Solution()
        print(solver.maxDepth(root))
        assert solver.maxDepth(root) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
