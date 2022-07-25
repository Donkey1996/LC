import sys
from collections import deque, defaultdict
from typing import Optional

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree

"""
112. Path Sum
Easy

Given the root of a binary tree and an integer targetSum, return true if 
the tree has a root-to-leaf path such that adding up all the values along 
the path equals targetSum.

A leaf is a node with no children.
"""


class Solution:
    """
    BFS/DFS
    """

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        q = deque([(root, root.val)])
        flag = False
        while q:
            cur, cur_val = q.popleft()
            if cur.left is None and cur.right is None and cur_val == targetSum:
                flag = True
                break
            if cur.left:
                q.append((cur.left, cur_val + cur.left.val))
            if cur.right:
                q.append((cur.right, cur_val + cur.right.val))
        return flag


"""
recursion
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    # 1:27
    def hasPathSum(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True
        
        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

"""


def main():
    tests = [
        {
            "vals": [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],
            "target": 22,
            "result": True,
        }
    ]

    i = 0
    for test in tests:
        i += 1
        vals = test["vals"]
        root = list_to_tree(vals)
        solver = Solution()
        assert solver.hasPathSum(root, test["target"]) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
