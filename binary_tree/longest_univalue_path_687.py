import sys
from typing import Any, Callable, Dict, List, Optional, Tuple, Union
from collections import deque
sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree
from utils.serializer import Serializer

"""
687. Longest Univalue Path
Medium

Given the root of a binary tree, return the length of the longest path, 
where each node in the path has the same value. 
This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.
"""
class Solution:
    """
    https://leetcode.com/problems/longest-univalue-path/discuss/108142/Python-Simple-to-Understand
    学
    """
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        self.traverse(root)
        return self.longest
        
    def traverse(self, root):
        if root is None:
            return 0
        l = self.traverse(root.left)
        r = self.traverse(root.right)
        if root.left and root.left.val == root.val:
            l = l + 1
        else:
            l = 0
        if root.right and root.right.val == root.val:
            r = r + 1
        else:
            r = 0
        self.longest = max(self.longest, l+r)
        return max(l, r)

def main():
    tests = [
        {"vals": [1,4,5,4,4,None,5], "result": 2},
        {"vals": [5,4,5,1,1,None,5], "result": 2},
        {"vals": [], "result": 0},
    ]

    i = 0
    for test in tests:
        i += 1
        vals = test["vals"]
        root = list_to_tree(vals)
        solver = Solution()
        print(solver.longestUnivaluePath(root))
        assert solver.longestUnivaluePath(root) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
