from re import sub
import sys
from collections import deque, defaultdict
from typing import Optional
from regex import R

from sympy import rootof

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree

"""
572. Subtree of Another Tree
Easy

Given the roots of two binary trees root and subRoot, 
return true if there is a subtree of root with the same structure
 and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree 
and all of this node's descendants. The tree tree could also be considered 
as a subtree of itself.
"""


class Solution:
    def isSubtree(self, root, subRoot):
        if root is None:
            return False
        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
            or self.is_same(root, subRoot)
        )

    def is_same(self, root1, root2):
        if not (root1 and root2):
            return root1 is root2
        return (
            self.is_same(root1.left, root2.left)
            and self.is_same(root1.right, root2.right)
            and root1.val == root2.val
        )

    # wrong
    # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     g_root = self.to_dict(root)
    #     g_sub = self.to_dict(subRoot)
    #     print(g_root)
    #     print(g_sub)
    #     flag = True
    #     for i in g_sub:
    #         if not i in g_root:
    #             flag = False
    #             break
    #         for j in g_sub[i]:
    #             if not j in g_root[i]:
    #                 flag = False
    #                 break
    #             continue
    #     return flag

    # def to_dict(self, root):
    #     g = defaultdict(list)
    #     q = deque([root])
    #     while q:
    #         node = q.popleft()
    #         if node.left:
    #             g[node.val].append(node.left.val)
    #             q.append(node.left)
    #         else:
    #             g[node.val].append('Null Left')
    #         if node.right:
    #             g[node.val].append(node.right.val)
    #             q.append(node.right)
    #         else:
    #             g[node.val].append('Null Right')
    #     return g


def main():
    tests = [
        {"root": [3, 4, 5, 1, 2], "subtree": [4, 1, 2], "result": True,},
        {
            "root": [3, 4, 5, 1, 2, None, None, None, None, 0],
            "subtree": [4, 1, 2],
            "result": False,
        },
        {"root": [1, 1], "subtree": [1], "result": True},
    ]

    i = 0
    for test in tests:
        i += 1
        root = list_to_tree(test["root"])
        sub_root = list_to_tree(test["subtree"])
        solver = Solution()
        assert solver.isSubtree(root, sub_root) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
