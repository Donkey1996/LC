from importlib.resources import path
from operator import is_
import sys
from collections import deque, defaultdict
from typing import Optional
from copy import deepcopy

from sympy import is_increasing

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree

"""
236. Lowest Common Ancestor of a Binary Tree
Medium
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if self.is_in_tree(p, q):
            return p
        if self.is_in_tree(q, p):
            return q
        if self.is_in_tree(root.left, p) and self.is_in_tree(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        if self.is_in_tree(root.right, p) and self.is_in_tree(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)
        return root

    def is_in_tree(self, root: "TreeNode", p: "TreeNode") -> bool:
        if root is None:
            return False
        if root == p:
            return True
        return self.is_in_tree(root.left, p) or self.is_in_tree(root.right, p)
