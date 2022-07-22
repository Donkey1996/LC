import sys
from collections import deque, defaultdict
from typing import Optional


from sympy import rootof

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree

"""
965. Univalued Binary Tree
Easy

A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, 
or false otherwise.
"""


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.equal_to(root, root.val)

    def equal_to(self, root, val):
        if not root:
            return True
        return (
            root.val == val
            and self.equal_to(root.left, val)
            and self.equal_to(root.right, val)
        )


def main():
    tests = [
        {"root": [3, 4, 5, 1, 2], "result": False},
        {"root": [1, 1, 1], "result": True},
        {"root": [3], "result": True},
        {"root": [], "result": True},
        {"root": [2, 2, 2, 2, 2, 3], "result": False},
        {"root": [1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1,], "result": False},
    ]

    i = 0
    for test in tests:
        i += 1
        root = list_to_tree(test["root"])
        solver = Solution()
        assert solver.isUnivalTree(root) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
