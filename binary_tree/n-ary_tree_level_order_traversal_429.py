import sys
from collections import deque
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.NaryNode import NaryNode

"""
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

"""


class Solution:
    """
    BFS
    """

    def levelOrder(self, root: NaryNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            n = len(q)
            current_level = []
            for i in range(n):
                current = q.popleft()
                q += current.children
                current_level += [current.val]
            res += [current_level]
        return res


def main():
    node5 = NaryNode(5, [])
    node6 = NaryNode(6, [])
    node3 = NaryNode(3, [node5, node6])
    node2 = NaryNode(2, [])
    node4 = NaryNode(4, [])
    node1 = NaryNode(1, [node3, node2, node4])
    solver = Solution()
    print(solver.levelOrder(node1))


if __name__ == "__main__":
    main()
