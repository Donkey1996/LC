import sys
from collections import deque, defaultdict
from typing import Optional

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree

"""
1325. Delete Leaves With a Given Value
Medium

Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a 
leaf node and has the value target, it should also be deleted 
(you need to continue doing that until you cannot).
"""


class Solution:
    def removeLeafNodes(self, root, target):
        if root is None:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if root.left is None and root.right is None and root.val == target:
            return None
        return root
