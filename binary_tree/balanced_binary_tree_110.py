import sys
from collections import deque, defaultdict
from typing import Optional

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree

"""
110. Balanced Binary Tree
Easy

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height 
by no more than 1.
"""


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return (
            abs(self.get_depth(root.left) - self.get_depth(root.right)) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )

    def get_depth(self, root):
        if root is None:
            return 0
        return max(self.get_depth(root.left), self.get_depth(root.right)) + 1


def main():
    tests = [
        {"vals": [3, 9, 20, None, None, 15, 7], "result": True,},
        {"vals": [1, 2, 2, 3, 3, None, None, 4, 4], "result": False},
        {"vals": [], "result": True},
        {"vals": [1, 2, 2, 3, None, None, 3, 4, None, None, 4], "result": False},
    ]

    i = 0
    for test in tests:
        i += 1
        vals = test["vals"]
        root = list_to_tree(vals)
        solver = Solution()
        print(solver.get_depth(root))
        assert solver.isBalanced(root) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
