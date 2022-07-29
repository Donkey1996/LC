from operator import is_
import sys
from collections import deque, defaultdict
from typing import Optional
from copy import deepcopy

from sympy import is_increasing

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
    '''
    Let large = max(p.val, q.val), small = min(p.val, q.val).
    We keep iterate root in our BST:
    If root.val > large then both node p and q belong to the left subtree, go to left by root = root.left.
    If root.val < small then both node p and q belong to the right subtree, go to right by root = root.right.
    Now, small <= root.val <= large the current root is the LCA between q and p.

    
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

    def is_in_tree(self, root, p):
        if root is None:
            return False
        if root == p:
            return True
        return self.is_in_tree(root.left, p) or self.is_in_tree(root.right, p)
