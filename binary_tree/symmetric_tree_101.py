import sys
from collections import deque, defaultdict
from typing import Optional

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree

"""
101. Symmetric Tree
Easy

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

"""


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_mirror(root, root)

    def is_mirror(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return (
            root1.val == root2.val
            and self.is_mirror(root1.left, root2.right)
            and self.is_mirror(root1.right, root2.left)
        )


def main():
    tests = [
        {"vals": [1, 2, 2, 3, 4, 4, 3], "result": True},
        {"vals": [1, 2, 2, None, 3, None, 3], "result": False},
    ]
    i = 0
    for test in tests:
        i += 1
        vals = test["vals"]
        root = list_to_tree(vals)
        solver = Solution()
        assert solver.isSymmetric(root) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
