import sys
from collections import deque, defaultdict
from typing import Optional

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree

"""
111. Minimum Depth of Binary Tree
Easy

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down 
to the nearest leaf node.

Note: A leaf is a node with no children.
"""


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def get_depth(self, root):
        if root is None:
            return 0
        return max(self.get_depth(root.left), self.get_depth(root.right)) + 1


def main():
    tests = [
        {"vals": [3, 9, 20, None, None, 15, 7], "result": 2,},
        {
            "vals": [
                2,
                None,
                3,
                None,
                None,
                None,
                4,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                5,
            ],
            "result": 4,
        },
        {"vals": [-9, -3, 2, None, 4, 4, 0, -6, None, -5], "result": 3},
    ]

    i = 0
    for test in tests:
        i += 1
        vals = test["vals"]
        root = list_to_tree(vals)
        solver = Solution()
        print(solver.minDepth(root))
        assert solver.minDepth(root) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
