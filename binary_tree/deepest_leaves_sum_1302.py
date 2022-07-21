import sys
from collections import deque, defaultdict
from typing import Optional

sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree
"""
1302. Deepest Leaves Sum
Medium

Given the root of a binary tree, return the sum of values of its deepest leaves.

"""

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        visited = defaultdict(list)
        q = deque([(root, 0)]) #node, depth
        while q:
            node, depth = q.popleft()
            visited[depth].append(node.val)
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
        return sum(visited[sorted(visited)[-1]])

def main():
    tests = [
        {"vals": [1,2,3,4,5,None,6,7,None,None,None,None,None,None,8], "result": 15},
        {"vals": [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5], "result": 19}
    ]

    i = 0
    for test in tests:
        i += 1
        vals = test["vals"]
        root = list_to_tree(vals)
        solver = Solution()
        assert solver.deepestLeavesSum(root) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
