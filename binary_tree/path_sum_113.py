import sys
from collections import deque, defaultdict
from typing import Optional, List
from copy import deepcopy

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree

"""
113. Path Sum II
Medium

Given the root of a binary tree and an integer targetSum, 
return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node.
A leaf is a node with no children.
"""


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if root is None:
            return []
        q = deque([(root, root.val, [root.val])])
        while q:
            cur, cur_val, cur_path = q.popleft()
            if cur.left:
                path = deepcopy(cur_path)
                path.append(cur.left.val)
                q.append((cur.left, cur_val + cur.left.val, path))
            if cur.right:
                path = deepcopy(cur_path)
                path.append(cur.right.val)
                q.append((cur.right, cur_val + cur.right.val, path))
            if cur.left is None and cur.right is None and cur_val == targetSum:
                res.append(cur_path)
        return res


def main():
    tests = [
        {
            "vals": [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1],
            "target": 22,
            "result": [[5, 4, 11, 2], [5, 8, 4, 5]],
        },
        {"vals": [1, 2, 3], "target": 5, "result": [],},
        {"vals": [1, 2], "target": 0, "result": [],},
    ]

    i = 0
    for test in tests:
        i += 1
        vals = test["vals"]
        root = list_to_tree(vals)
        solver = Solution()
        print(solver.pathSum(root, test["target"]))
        assert solver.pathSum(root, test["target"]) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
