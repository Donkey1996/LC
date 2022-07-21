from email.policy import default
import sys
from collections import deque, defaultdict
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from sympy import Q

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree

"""
987. Vertical Order Traversal of a Binary Tree
HARD

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.
"""


class Solution:
    """
    BFS
    """

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # g = defaultdict(list)
        # q = deque([(root, 0)]) #node, index
        # while q:
        #     temp_g = defaultdict(list)
        #     for i in range(len(q)):
        #         node, index = q.popleft()
        #         temp_g[index].append(node.val)
        #         if node.left:
        #             q.append((node.left, index-1))
        #         if node.right:
        #             q.append((node.right, index+1))
        #     for index in temp_g:
        #         g[index].extend(sorted(temp_g[index]))
        # return [g[index] for index in sorted(g)]
        g = defaultdict(list)
        q = [(root, 0)]
        while q:
            temp_g = defaultdict(list)
            for i in range(len(q)):
                node, index = q.pop(0)
                temp_g[index].append(node.val)
                if node.left:
                    q.append((node.left, index - 1))
                if node.right:
                    q.append((node.right, index + 1))
            for index in temp_g:
                g[index].extend(sorted(temp_g[index]))
        return [g[i] for i in sorted(g)]


def main():
    tests = [
        {"vals": [3, 9, 20, None, None, 15, 7], "traversal": [[9], [3, 15], [20], [7]]},
        {"vals": [1, 2, 3, 4, 5, 6, 7], "traversal": [[4], [2], [1, 5, 6], [3], [7]]},
    ]

    i = 0
    for test in tests:
        i += 1
        vals = test["vals"]
        root = list_to_tree(vals)
        solver = Solution()
        print(solver.verticalTraversal(root))
        assert solver.verticalTraversal(root) == test["traversal"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
