import sys
from typing import Any, Callable, Dict, List, Optional, Tuple, Union
from collections import deque

from sklearn.compose import TransformedTargetRegressor

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree
from utils.serializer import Serializer

"""
437. Path Sum III
Medium

Given the root of a binary tree and an integer targetSum, 
return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards 
(i.e., traveling only from parent nodes to child nodes).
"""


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum) -> int:
        if root is None:
            return 0
        return (
            self.pathSum(root.left, targetSum)
            + self.dfs(root, targetSum)
            + self.pathSum(root.right, targetSum)
        )

    def dfs(self, root, target):
        # root to node sum
        if root is None:
            return 0
        res = 0
        q = deque([[root, root.val]])
        while q:
            cur, cur_sum = q.popleft()
            if cur_sum == target:
                res += 1
            if cur.left:
                q.append([cur.left, cur_sum + cur.left.val])
            if cur.right:
                q.append([cur.right, cur_sum + cur.right.val])
        return res


def main():
    tests = [
        {
            "vals": [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1],
            "targetSum": 8,
            "result": 3,
        },
        {
            "vals": [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1],
            "targetSum": 22,
            "result": 3,
        },
        {"vals": [], "targetSum": 0, "result": 0},
    ]

    i = 0
    for test in tests:
        i += 1
        vals = test["vals"]
        root = list_to_tree(vals)
        solver = Solution()
        print(solver.pathSum(root, test["targetSum"]))
        assert solver.pathSum(root, test["targetSum"]) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
