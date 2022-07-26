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
    """
    Approach 1: Dynamic Programming
    Intuition

    Let's try to cover every node, starting from the top of the tree and working down. Every node considered must be covered by a camera at that node or some neighbor.

    Because cameras only care about local state, we can hope to leverage this fact for an efficient solution. Specifically, when deciding to place a camera at a node, we might have placed cameras to cover some subset of this node, its left child, and its right child already.

    Algorithm

    Let solve(node) be some information about how many cameras it takes to cover the subtree at this node in various states. There are essentially 3 states:

    [State 0] Strict subtree: All the nodes below this node are covered, but not this node.
    [State 1] Normal subtree: All the nodes below and including this node are covered, but there is no camera here.
    [State 2] Placed camera: All the nodes below and including this node are covered, and there is a camera here (which may cover nodes above this node).
    Once we frame the problem in this way, the answer falls out:

    To cover a strict subtree, the children of this node must be in state 1.
    To cover a normal subtree without placing a camera here, the children of this node must be in states 1 or 2, and at least one of those children must be in state 2.
    To cover the subtree when placing a camera here, the children can be in any state.
    
    """

    def minCameraCover(self, root):
        return min(self.solve(root)[1:])

    def solve(self, root):
        if root is None:
            return 0, 0, float("inf")
        L = self.solve(root.left)
        R = self.solve(root.right)
        dp0 = L[1] + R[1]
        dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
        dp2 = 1 + min(L) + min(R)
        return dp0, dp1, dp2


def main():
    tests = [
        {"root": [0, 0, None, 0, 0], "result": 1},
        {
            "root": [
                0,
                0,
                None,
                0,
                None,
                None,
                None,
                0,
                None,
                None,
                None,
                None,
                None,
                0,
            ],
            "result": 2,
        },
    ]

    i = 0
    for test in tests:
        i += 1
        root = list_to_tree(test["root"])
        solver = Solution()
        print(solver.minCameraCover(root))
        assert solver.minCameraCover(root) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
