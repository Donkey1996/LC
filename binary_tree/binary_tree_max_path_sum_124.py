import sys
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from regex import R
from sympy import Max

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree


class Solution:
    """
    https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram
    学
    """

    def maxPathSum(self, root):
        res = -float("inf")

        def utility(root):
            nonlocal res
            if root is None:
                return 0
            left = max(0, utility(root.left))
            right = max(0, utility(root.right))
            cur_path = root.val + left + right
            res = max(res, cur_path)
            return root.val + max(left, right)

        if root is None:
            return 0
        utility(root)
        return res


def main():
    tests = [{"vals": [1, 2, 3], "result": 6}]
    i = 0
    for test in tests:
        i += 1
        vals = test["vals"]
        root = list_to_tree(vals)
        solver = Solution()
        print(solver.maxPathSum(root))
        assert solver.maxPathSum(root) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
