import sys
from collections import deque, defaultdict
from typing import Optional

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree

"""
1302. Deepest Leaves Sum
Medium

Given the root of a binary tree, return the sum of values of its deepest leaves.

"""


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.traversal(p) == self.traversal(q)

    def traversal(self, root):
        res = []
        self.search(root, res)
        return res

    def search(self, root, res):
        if root:
            res.append(root.val)
            self.search(root.left, res)

            self.search(root.right, res)
        else:
            res.append("Null")

    # def postorder_traversal(self, root):
    #     res = []
    #     self.postorder_search(root, res)
    #     return res

    # def postorder_search(self, root, res):
    #     if root:
    #         self.postorder_search(root.left, res)
    #         self.postorder_search(root.right, res)
    #         res.append(root.val)


def main():
    tests = [
        {
            "p": [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, None, None, 8],
            "q": [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, None, None, 8],
            "result": True,
        },
        {"p": [1, 1], "q": [1, None, 1], "result": False},
    ]

    i = 0
    for test in tests:
        i += 1
        vals_p = test["p"]
        vals_q = test["q"]
        root_p = list_to_tree(vals_p)
        root_q = list_to_tree(vals_q)
        solver = Solution()
        assert solver.isSameTree(root_p, root_q) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
