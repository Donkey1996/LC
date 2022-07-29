import sys
from collections import deque, defaultdict
from typing import Optional
from copy import deepcopy

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree

"""
129. Sum Root to Leaf Numbers
Medium

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that 
the answer will fit in a 32-bit integer.

A leaf node is a node with no children.
"""


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        res = []
        q = deque([[root, [root.val]]])
        while q:
            cur, cur_path = q.popleft()
            if cur.left is None and cur.right is None:
                res.append(self.list_to_int(cur_path))
            if cur.left:
                path = deepcopy(cur_path)
                path.append(cur.left.val)
                q.append([cur.left, path])
            if cur.right:
                path = deepcopy(cur_path)
                path.append(cur.right.val)
                q.append([cur.right, path])
        return sum(res)

    def list_to_int(self, path):
        if len(path) == 0:
            return 0
        string = ""
        for i in path:
            string += str(i)
        return int(string)


def main():
    tests = [
        {"vals": [1, 2, 3], "result": 25,},
        {"vals": [4, 9, 0, 5, 1], "result": 1026},
    ]
    i = 0
    for test in tests:
        i += 1
        vals = test["vals"]
        root = list_to_tree(vals)
        solver = Solution()
        print(solver.sumNumbers(root))
        assert solver.sumNumbers(root) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
