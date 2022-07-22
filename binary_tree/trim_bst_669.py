import sys
from collections import deque, defaultdict
from typing import Optional

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree

"""
669. Trim a Binary Search Tree
Medium

Given the root of a binary search tree and the lowest and highest boundaries as 
low and high, trim the tree so that all its elements lies in [low, high]. 
Trimming the tree should not change the relative structure of the elements that 
will remain in the tree (i.e., any node's descendant should remain a descendant). 
It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. 
Note that the root may change depending on the given bounds.
"""


class Solution:
    """
    -If the val of current node is smaller than L, 
        abandon the left sub-tree and trim its right sub-tree
    -If the val of current node is greater than R, 
        abandon the right sub-tree and trim its left sub-tree
    -Else, recursively trim its left and right sub-tree and return the root
    """

    # 学
    def trimBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
