import sys
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from regex import R
sys.path.insert(0, "/home/jerrymengxiao/dev/LC")

from utils.TreeNode import TreeNode, list_to_tree

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self._find(root, res)
        return res

    def _find(self, root, res):
        if root:
            self._find(root.left, res)
            res.append(root.val)
            self._find(root.right, res)

def main():
    tests = [
        {"vals": [1, 2, 3, 4], "traversal": [4,2,1,3]}
    ]
    i = 0
    for test in tests:
        i += 1
        vals = test["vals"]
        root = list_to_tree(vals)
        print(root.val)
        print(root.left.val)
        print(root.right.val)
        print(root.left.left.val)
        solver = Solution()
        print(solver.inorderTraversal(root))
        assert solver.inorderTraversal(root) == test["traversal"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
