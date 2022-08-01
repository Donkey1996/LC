import sys
from collections import deque, defaultdict
from typing import Optional

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree
from utils.serializer import Serializer

"""
508. Most Frequent Subtree Sum
Medium

Given the root of a binary tree, return the most frequent subtree sum. 
If there is a tie, return all the values with the highest frequency in any order.

The subtree sum of a node is defined as the sum of all the node values formed by 
the subtree rooted at that node (including the node itself).
"""


class Solution:
    def findFrequentTreeSum(self, root):
        q = deque([root])
        sum_list = {}
        while q:
            cur_node = q.popleft()
            cur_sum = self.get_sum_subtree(cur_node)
            if cur_sum in sum_list:
                sum_list[cur_sum] += 1
            else:
                sum_list[cur_sum] = 1
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
        highest_frequency = sorted(sum_list.values())[-1]
        res = []
        for sum in sum_list:
            if sum_list[sum] == highest_frequency:
                res.append(sum)
        return res

    def get_sum_subtree(self, root):
        if root is None:
            return 0
        return (
            root.val
            + self.get_sum_subtree(root.left)
            + self.get_sum_subtree(root.right)
        )


def main():
    tests = [
        {"vals": [5, 2, -3], "result": [2, -3, 4],},
        {"vals": [5, 2, -5], "result": [2],},
    ]

    i = 0
    for test in tests:
        i += 1
        vals = test["vals"]
        root = list_to_tree(vals)
        solver = Solution()
        print(solver.findFrequentTreeSum(root))
        # assert solver.findFrequentTreeSum(root) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
