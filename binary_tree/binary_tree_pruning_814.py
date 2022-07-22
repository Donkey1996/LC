import sys
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree

"""
814. Binary Tree Pruning
Medium

Given the root of a binary tree, return the same tree where every subtree 
(of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.
"""


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        if not self.is_in_tree(root.left):
            root.left = None
        if not self.is_in_tree(root.right):
            root.right = None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        return root

    def is_in_tree(self, root, x=1):
        if root:
            return (
                root.val == x
                or self.is_in_tree(root.left, x)
                or self.is_in_tree(root.right, x)
            )
        return False


def main():
    tests = [{"vals": [1, None, 0, 0, 1], "result": [1, None, 0, None, 1]}]
    i = 0
    for test in tests:
        i += 1
        vals = test["vals"]
        root = list_to_tree(vals)
        solver = Solution()
        assert solver.pruneTree(root) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
