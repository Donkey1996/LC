import sys
from collections import deque, defaultdict
from typing import Optional
from copy import deepcopy

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree

"""
235. Lowest Common Ancestor of a Binary Search Tree
Easy
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two 
given nodes in the BST.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is 
defined between two nodes p and q as the lowest node in T that has both p and q as 
descendants (where we allow a node to be a descendant of itself)."
"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

def main():
    tests = [
        {
            "vals": [6,2,8,0,4,7,9,None,None,3,5], 
            "p": 2,
            "q": 8,
            "result": 6,
        },
        {
            "vals": [6,2,8,0,4,7,9,None,None,3,5], 
            "p": 2,
            "q" : 4,
            "result": 2
        },
    ]
    i = 0
    for test in tests:
        i += 1
        vals = test["vals"]
        root = list_to_tree(vals)
        solver = Solution()
        assert solver.lowestCommonAncestor(root) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
