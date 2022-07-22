"""
872. Leaf-Similar Trees
Easy

Consider all the leaves of a binary tree, from left to right order, 
the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are 
leaf-similar.
"""


import sys
from collections import deque, defaultdict
from typing import Optional

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree


class Solution:
    def leafSimilar(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is q:
            return True
        return self.get_leaves(p) == self.get_leaves(q)

    def get_leaves(self, root):
        res = []
        q = deque([root])
        while q:
            cur = q.pop()
            if not cur.left and not cur.right:
                res.append(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return res


def main():
    tests = [
        {
            "p": [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, None, None, 8],
            "q": [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, None, None, 8],
            "result": True,
        },
        {"p": [1, 1], "q": [1, None, 1], "result": True},
        {
            "p": [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4],
            "q": [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8],
            "result": True,
        },
        {"p": [1, 2, 3], "q": [1, 3, 2], "result": False},
    ]

    i = 0
    for test in tests:
        i += 1
        vals_p = test["p"]
        vals_q = test["q"]
        root_p = list_to_tree(vals_p)
        root_q = list_to_tree(vals_q)
        solver = Solution()
        print(solver.get_leaves(root_p))
        print(solver.get_leaves(root_q))
        assert solver.leafSimilar(root_p, root_q) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
