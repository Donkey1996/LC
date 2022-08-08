import sys
from collections import deque, defaultdict
from typing import Optional

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree

"""
337. House Robber III
Medium

The thief has found himself a new place for his thievery again. 
There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. 
After a tour, the smart thief realized that all houses in this place form a binary tree. 
It will automatically contact the police if two directly-linked houses were broken into 
on the same night.

Given the root of the binary tree, return the maximum amount of money the thief 
can rob without alerting the police.
"""


class Solution:
    """
    https://leetcode.com/problems/house-robber-iii/discuss/376297/Python3-Dynamic-Programming-%2B-Depth-First-Search
    """

    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root))

    def dfs(self, root):
        # state1: rob this root
        # state2: not rob this root
        if root is None:
            return 0, 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        sum1 = root.val + left[1] + right[1]
        sum2 = max(left[0], left[1]) + max(right[0], right[1])
        return sum1, sum2


def main():
    tests = [
        {"vals": [3, 2, 3, None, 3, None, 1], "result": 7,},
        {"vals": [3, 4, 5, 1, 3, None, 1], "result": 9},
    ]

    i = 0
    for test in tests:
        i += 1
        vals = test["vals"]
        root = list_to_tree(vals)
        solver = Solution()
        print(solver.rob(root))
        assert solver.rob(root) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
