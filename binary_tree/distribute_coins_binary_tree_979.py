import sys
from collections import deque, defaultdict
from typing import Optional

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree

"""
979. Distribute Coins in Binary Tree
Medium

You are given the root of a binary tree with n nodes where each node in the tree has node.val 
coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. 
A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.
"""


class Solution:
    """
    use abs() to calculate the movement needed.
    """

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root is None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.res += abs(left) + abs(right)
        return root.val + left + right - 1


def main():
    tests = [
        {"vals": [3, 0, 0], "result": 2},
        {"vals": [0, 3, 0], "result": 3},
    ]

    i = 0
    for test in tests:
        i += 1
        vals = test["vals"]
        root = list_to_tree(vals)
        solver = Solution()
        print(solver.distributeCoins(root))
        assert solver.distributeCoins(root) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
